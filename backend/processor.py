"""
Submission processor — validates, sanitizes, and transforms structured
data into repository-compliant Markdown for cannabis-legalization chapters.

Pure stdlib — no external dependencies.
"""

from __future__ import annotations

import re
from typing import Any


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = ("chapter_number", "title", "content")

# chapter_number 0 is valid (metadata chapter) — only None is missing
_FALSY_OK = frozenset({"chapter_number"})
VALID_CITATION_RE = re.compile(r"\[@[a-zA-Z0-9_\-:]+\]")
STRIP_TAGS_RE = re.compile(r"<[^>]*>")


class ValidationError(ValueError):
    """Raised when a submission fails validation."""


def validate_submission(data: dict[str, Any]) -> None:
    """Validate a submission dict. Raises ValidationError on failure."""
    missing = []
    for f in REQUIRED_FIELDS:
        val = data.get(f)
        if f in _FALSY_OK:
            if val is None or not isinstance(val, int):
                missing.append(f)
        elif not val:
            # content may be empty string if sections are provided
            if f == "content" and isinstance(data.get("sections"), list) and len(data["sections"]) > 0:
                continue
            missing.append(f)

    if missing:
        raise ValidationError(
            f"Missing required fields: {', '.join(missing)}"
        )

    chapter_number = data.get("chapter_number")
    if not isinstance(chapter_number, int) or not (0 <= chapter_number <= 99):
        raise ValidationError(
            f"chapter_number must be an integer 0-99, got {chapter_number!r}"
        )

    title = data.get("title", "")
    if not isinstance(title, str) or not title.strip():
        raise ValidationError("title must be a non-empty string")

    content = data.get("content", "")
    if not isinstance(content, str):
        raise ValidationError("content must be a string")
    has_sections = isinstance(data.get("sections"), list) and len(data["sections"]) > 0
    if not content.strip() and not has_sections:
        raise ValidationError("content must be a non-empty string")

    # Optional fields
    subtitle = data.get("subtitle")
    if subtitle is not None and not isinstance(subtitle, str):
        raise ValidationError("subtitle must be a string if provided")

    citations = data.get("citations")
    if citations is not None:
        if not isinstance(citations, list):
            raise ValidationError("citations must be a list if provided")
        for i, c in enumerate(citations):
            if not isinstance(c, str) or not VALID_CITATION_RE.match(c):
                raise ValidationError(
                    f"citations[{i}] must be in [@key] format, got {c!r}"
                )


# ---------------------------------------------------------------------------
# Sanitization
# ---------------------------------------------------------------------------

def sanitize_text(text: str) -> str:
    """Strip HTML tags, normalize whitespace, and strip per-line whitespace."""
    text = STRIP_TAGS_RE.sub("", text)
    # Strip leading/trailing whitespace from each line
    text = "\n".join(line.strip() for line in text.splitlines())
    # Collapse multiple blank lines into at most one
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------

HEADING_PREFIX = {0: "# ", 1: "## ", 2: "### ", 3: "#### "}


def _format_section(heading: str, body: str, level: int = 1) -> str:
    """Format a single section at the given heading level."""
    prefix = HEADING_PREFIX.get(level, "## ")
    return f"{prefix}{heading}\n\n{body}"


def generate_markdown(data: dict[str, Any]) -> str:
    """Transform validated submission data into repository-compliant Markdown.

    Conventions:
    - H1 for chapter title (may include LaTeX \\newpage before)
    - H2+ for sections
    - Citations kept as [@key]
    - Tables use markdown pipe format
    - Supports optional frontmatter passthrough
    """
    lines: list[str] = []

    # Optional LaTeX page break before chapter
    if data.get("newpage", False):
        lines.append("\\newpage\n")

    # Chapter title (H1)
    title = sanitize_text(data["title"])
    lines.append(f"# {title}\n")

    # Optional subtitle block
    subtitle = data.get("subtitle")
    if subtitle:
        lines.append(f"> **{sanitize_text(subtitle)}**\n")

    # Content — may be a plain string or structured sections
    content = data.get("content", "")
    sections = data.get("sections")

    if isinstance(content, str) and content.strip():
        lines.append(sanitize_text(content))
    elif isinstance(sections, list):
        for sec in sections:
            if not isinstance(sec, dict):
                continue
            heading = sanitize_text(sec.get("heading", ""))
            body = sanitize_text(sec.get("body", ""))
            level = sec.get("level", 1)
            if heading and body:
                lines.append(_format_section(heading, body, level))
            elif body:
                lines.append(body)

    # Citations appendix at the bottom
    citations = data.get("citations")
    if citations and isinstance(citations, list):
        lines.append("\n### Referências do capítulo\n")
        lines.append(
            "As referências completas encontram-se em "
            "[`references.bib`](../../references.bib).\n"
        )
        for c in citations:
            lines.append(f"- {c}")

    return "\n".join(lines) + "\n"


def process_submission(data: dict[str, Any]) -> dict[str, Any]:
    """Full pipeline: validate → sanitize → generate markdown."""
    validate_submission(data)
    markdown = generate_markdown(data)
    return {
        "chapter_number": data["chapter_number"],
        "title": sanitize_text(data["title"]),
        "markdown": markdown,
    }
