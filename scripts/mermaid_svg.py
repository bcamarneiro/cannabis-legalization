#!/usr/bin/env python3
"""
Mermaid to SVG Serializer - Convert Mermaid diagrams to SVG strings.

This module provides functionality to serialize Mermaid diagram definitions
to SVG format without canvas dependencies, suitable for embedding in documents
or web pages.

Usage:
    from mermaid_svg import MermaidSerializer
    
    # Simple conversion
    serializer = MermaidSerializer()
    svg = serializer.to_svg("graph TB; A --> B")
    
    # From file
    svg = serializer.from_file("diagrams/flowchart.mmd")
    
    # CLI
    python3 mermaid_svg.py input.mmd output.svg
"""

import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Optional


class MermaidSerializer:
    """
    Serialize Mermaid diagrams to SVG format.
    
    Uses the Mermaid CLI (mmdc) to render diagrams as SVG strings,
    providing an alternative to PNG rendering for document integration.
    """
    
    def __init__(self, width: int = 1200, height: int = 800, 
                 background: str = "transparent"):
        """
        Initialize the Mermaid serializer.
        
        Args:
            width: SVG viewport width in pixels (default: 1200)
            height: SVG viewport height in pixels (default: 800)
            background: Background color (default: "transparent")
        """
        self.width = width
        self.height = height
        self.background = background
        self._mmdc_path = self._find_mmdc()
    
    def _find_mmdc(self) -> str:
        """Find the Mermaid CLI executable."""
        # Try common locations
        paths_to_try = [
            "mmdc",
            "/usr/local/bin/mmdc",
            "/usr/bin/mmdc",
        ]
        
        for path in paths_to_try:
            try:
                result = subprocess.run(
                    [path, "--version"],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    return path
            except (subprocess.SubprocessError, FileNotFoundError):
                continue
        
        raise RuntimeError(
            "Mermaid CLI (mmdc) not found. Install with: npm install -g @mermaid-js/mermaid-cli"
        )
    
    def to_svg(self, mermaid_code: str, title: Optional[str] = None) -> str:
        """
        Convert Mermaid code to SVG string.
        
        Args:
            mermaid_code: Mermaid diagram definition
            title: Optional title for the SVG (adds <title> element)
        
        Returns:
            SVG string
        
        Raises:
            RuntimeError: If mmdc is not available or rendering fails
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)
            input_file = tmpdir_path / "diagram.mmd"
            output_file = tmpdir_path / "diagram.svg"
            
            # Write Mermaid code to temp file
            input_file.write_text(mermaid_code)
            
            # Render to SVG using mmdc
            cmd = [
                self._mmdc_path,
                "-i", str(input_file),
                "-o", str(output_file),
                "-b", self.background,
                "-w", str(self.width),
                "-H", str(self.height),
            ]
            
            try:
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode != 0:
                    raise RuntimeError(
                        f"Mermaid rendering failed: {result.stderr}"
                    )
                
            except subprocess.TimeoutExpired:
                raise RuntimeError("Mermaid rendering timed out after 60 seconds")
            
            # Read SVG output
            if not output_file.exists():
                raise RuntimeError("SVG file was not generated")
            
            svg_content = output_file.read_text()
            
            # Optionally add title element
            if title:
                svg_content = self._add_title(svg_content, title)
            
            return svg_content
    
    def _add_title(self, svg: str, title: str) -> str:
        """Add a <title> element to the SVG for accessibility."""
        # Find the opening <svg> tag and insert title after it
        svg_start = svg.find("<svg")
        if svg_start == -1:
            return svg
        
        # Find the end of the opening tag
        svg_tag_end = svg.find(">", svg_start)
        if svg_tag_end == -1:
            return svg
        
        # Insert title element
        title_element = f"\n  <title>{title}</title>\n"
        return svg[:svg_tag_end + 1] + title_element + svg[svg_tag_end + 1:]
    
    def from_file(self, mmd_path: str, title: Optional[str] = None) -> str:
        """
        Convert a Mermaid .mmd file to SVG string.
        
        Args:
            mmd_path: Path to the .mmd file
            title: Optional title for the SVG
        
        Returns:
            SVG string
        
        Raises:
            FileNotFoundError: If the .mmd file doesn't exist
        """
        mmd_file = Path(mmd_path)
        if not mmd_file.exists():
            raise FileNotFoundError(f"Mermaid file not found: {mmd_path}")
        
        mermaid_code = mmd_file.read_text()
        
        # Use filename as default title if not provided
        if title is None:
            title = mmd_file.stem.replace("-", " ").replace("_", " ").title()
        
        return self.to_svg(mermaid_code, title=title)
    
    def serialize_to_file(self, mmd_path: str, svg_path: str, 
                         title: Optional[str] = None) -> Path:
        """
        Convert a Mermaid file and save as SVG.
        
        Args:
            mmd_path: Path to input .mmd file
            svg_path: Path for output .svg file
            title: Optional title for the SVG
        
        Returns:
            Path to the created SVG file
        """
        svg_content = self.from_file(mmd_path, title=title)
        
        output_path = Path(svg_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(svg_content)
        
        return output_path


def main():
    """CLI interface for Mermaid to SVG conversion."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Convert Mermaid diagrams to SVG format"
    )
    parser.add_argument(
        "input",
        type=str,
        help="Input .mmd file"
    )
    parser.add_argument(
        "output",
        type=str,
        nargs="?",
        help="Output .svg file (default: input.svg)"
    )
    parser.add_argument(
        "--width", "-w",
        type=int,
        default=1200,
        help="SVG width in pixels (default: 1200)"
    )
    parser.add_argument(
        "--height", "-H",
        type=int,
        default=800,
        help="SVG height in pixels (default: 800)"
    )
    parser.add_argument(
        "--background", "-b",
        type=str,
        default="transparent",
        help="Background color (default: transparent)"
    )
    parser.add_argument(
        "--title", "-t",
        type=str,
        help="SVG title for accessibility"
    )
    
    args = parser.parse_args()
    
    # Determine output path
    if args.output:
        output_path = args.output
    else:
        input_path = Path(args.input)
        output_path = str(input_path.with_suffix(".svg"))
    
    # Convert
    try:
        serializer = MermaidSerializer(
            width=args.width,
            height=args.height,
            background=args.background
        )
        
        result_path = serializer.serialize_to_file(
            args.input,
            output_path,
            title=args.title
        )
        
        print(f"✓ Converted {args.input} → {result_path}")
        
    except FileNotFoundError as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
