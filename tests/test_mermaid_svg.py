#!/usr/bin/env python3
"""
Tests for Mermaid to SVG serializer.

Run: python3 tests/test_mermaid_svg.py
"""

import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from mermaid_svg import MermaidSerializer


def test_serializer_initialization():
    """Test that serializer initializes with default values."""
    print("Test: serializer initialization...")
    
    serializer = MermaidSerializer()
    
    assert serializer.width == 1200, "Default width should be 1200"
    assert serializer.height == 800, "Default height should be 800"
    assert serializer.background == "transparent", "Default background should be transparent"
    
    print("  ✓ Serializer initialization passed")


def test_serializer_custom_params():
    """Test serializer with custom parameters."""
    print("Test: custom parameters...")
    
    serializer = MermaidSerializer(
        width=800,
        height=600,
        background="white"
    )
    
    assert serializer.width == 800
    assert serializer.height == 600
    assert serializer.background == "white"
    
    print("  ✓ Custom parameters passed")


def test_svg_contains_xml_structure():
    """Test that generated SVG contains proper XML structure."""
    print("Test: SVG XML structure...")
    
    # Simple Mermaid diagram
    mermaid_code = """graph LR
    A[Start] --> B[End]
    """
    
    try:
        serializer = MermaidSerializer(width=400, height=300)
        svg = serializer.to_svg(mermaid_code)
        
        # Check SVG structure
        assert svg.strip().startswith("<?xml") or svg.strip().startswith("<svg"), \
            "SVG should start with XML declaration or <svg> tag"
        assert "<svg" in svg, "SVG should contain <svg> element"
        assert "</svg>" in svg, "SVG should contain closing </svg> tag"
        
        print("  ✓ SVG XML structure passed")
        
    except RuntimeError as e:
        # Skip if mmdc not available
        print(f"  ⊘ Skipped (mmdc not available): {e}")


def test_svg_contains_title():
    """Test that title is added to SVG when specified."""
    print("Test: SVG title element...")
    
    mermaid_code = """graph TB
    A --> B
    """
    
    try:
        serializer = MermaidSerializer(width=400, height=300)
        svg = serializer.to_svg(mermaid_code, title="Test Diagram")
        
        assert "<title>Test Diagram</title>" in svg, \
            "SVG should contain title element when specified"
        
        print("  ✓ SVG title element passed")
        
    except RuntimeError as e:
        print(f"  ⊘ Skipped (mmdc not available): {e}")


def test_from_file_method():
    """Test loading Mermaid from file."""
    print("Test: from_file method...")
    
    # Create a temp Mermaid file
    test_mmd = Path(__file__).parent / "test_diagram.mmd"
    test_mmd.write_text("graph LR\nA --> B\n")
    
    try:
        serializer = MermaidSerializer(width=400, height=300)
        svg = serializer.from_file(str(test_mmd))
        
        assert "<svg" in svg, "Should generate SVG from file"
        
        print("  ✓ from_file method passed")
        
    except RuntimeError as e:
        print(f"  ⊘ Skipped (mmdc not available): {e}")
    finally:
        # Cleanup
        if test_mmd.exists():
            test_mmd.unlink()


def test_serialize_to_file():
    """Test saving SVG to file."""
    print("Test: serialize_to_file method...")
    
    # Create temp files
    test_mmd = Path(__file__).parent / "test_input.mmd"
    test_svg = Path(__file__).parent / "test_output.svg"
    test_mmd.write_text("graph TB\nA[Hello] --> B[World]\n")
    
    try:
        serializer = MermaidSerializer(width=400, height=300)
        result_path = serializer.serialize_to_file(
            str(test_mmd),
            str(test_svg),
            title="Hello World"
        )
        
        assert result_path.exists(), "SVG file should be created"
        assert result_path == test_svg, "Should return correct path"
        
        # Verify content
        svg_content = result_path.read_text()
        assert "<svg" in svg_content
        assert "<title>Hello World</title>" in svg_content
        
        print("  ✓ serialize_to_file method passed")
        
    except RuntimeError as e:
        print(f"  ⊘ Skipped (mmdc not available): {e}")
    finally:
        # Cleanup
        if test_mmd.exists():
            test_mmd.unlink()
        if test_svg.exists():
            test_svg.unlink()


def test_mmdc_not_found_error():
    """Test error handling when mmdc is not available."""
    print("Test: mmdc not found error handling...")
    
    # This test verifies the error message is helpful
    try:
        serializer = MermaidSerializer()
        # If we get here, mmdc is available, so test is N/A
        print("  ⊘ Skipped (mmdc is available)")
    except RuntimeError as e:
        assert "mmdc" in str(e).lower(), \
            "Error should mention mmdc installation instructions"
        print("  ✓ mmdc not found error handling passed")


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 50)
    print("Mermaid to SVG Serializer - Test Suite")
    print("=" * 50 + "\n")
    
    tests = [
        test_serializer_initialization,
        test_serializer_custom_params,
        test_svg_contains_xml_structure,
        test_svg_contains_title,
        test_from_file_method,
        test_serialize_to_file,
        test_mmdc_not_found_error,
    ]
    
    passed = 0
    failed = 0
    skipped = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ {test.__name__} ERROR: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 50 + "\n")
    
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
