"""
Test suite for backend.processor — stdlib unittest (no pytest).

Usage:
    python3 -m unittest backend.tests.test_processor
"""

from __future__ import annotations

import unittest

from backend.processor import (
    ValidationError,
    generate_markdown,
    process_submission,
    sanitize_text,
    validate_submission,
)


# ---------------------------------------------------------------------------
# validate_submission
# ---------------------------------------------------------------------------

class TestValidateSubmission(unittest.TestCase):
    def test_valid_minimal(self) -> None:
        validate_submission(
            {"chapter_number": 1, "title": "Título", "content": "Corpo"}
        )

    def test_missing_required_field(self) -> None:
        with self.assertRaises(ValidationError) as ctx:
            validate_submission({"chapter_number": 3, "title": "Só"})
        self.assertIn("content", str(ctx.exception))

    def test_chapter_number_not_int(self) -> None:
        with self.assertRaises(ValidationError) as ctx:
            validate_submission(
                {"chapter_number": "um", "title": "X", "content": "Y"}
            )
        self.assertIn("chapter_number", str(ctx.exception))

    def test_chapter_number_out_of_range(self) -> None:
        with self.assertRaises(ValidationError):
            validate_submission(
                {"chapter_number": 100, "title": "X", "content": "Y"}
            )

    def test_title_empty(self) -> None:
        with self.assertRaises(ValidationError) as ctx:
            validate_submission(
                {"chapter_number": 1, "title": "   ", "content": "Y"}
            )
        self.assertIn("title", str(ctx.exception))

    def test_content_empty(self) -> None:
        with self.assertRaises(ValidationError) as ctx:
            validate_submission(
                {"chapter_number": 1, "title": "X", "content": ""}
            )
        self.assertIn("content", str(ctx.exception))

    def test_valid_with_citations(self) -> None:
        validate_submission(
            {
                "chapter_number": 2,
                "title": "Evidência",
                "content": "Texto.",
                "citations": ["[@smith2020]", "[@jones:42]"],
            }
        )

    def test_bad_citation_format(self) -> None:
        with self.assertRaises(ValidationError) as ctx:
            validate_submission(
                {
                    "chapter_number": 2,
                    "title": "Evidência",
                    "content": "Texto.",
                    "citations": ["smith2020"],
                }
            )
        self.assertIn("citations[0]", str(ctx.exception))

    def test_chapter_number_zero_allowed(self) -> None:
        validate_submission(
            {"chapter_number": 0, "title": "Metadata", "content": "---"}
        )


# ---------------------------------------------------------------------------
# sanitize_text
# ---------------------------------------------------------------------------

class TestSanitizeText(unittest.TestCase):
    def test_strips_html_tags(self) -> None:
        self.assertEqual(
            sanitize_text("<p>Hello <b>world</b></p>"),
            "Hello world",
        )

    def test_collapses_multiple_blank_lines(self) -> None:
        self.assertEqual(
            sanitize_text("A\n\n\n\nB"),
            "A\n\nB",
        )

    def test_trims_whitespace(self) -> None:
        self.assertEqual(sanitize_text("  hello  \n  world  "), "hello\nworld")

    def test_passthrough_plain_text(self) -> None:
        self.assertEqual(sanitize_text("Plain text."), "Plain text.")


# ---------------------------------------------------------------------------
# generate_markdown
# ---------------------------------------------------------------------------

class TestGenerateMarkdown(unittest.TestCase):
    def test_basic_chapter(self) -> None:
        md = generate_markdown(
            {
                "chapter_number": 1,
                "title": "Sumário Executivo",
                "content": "Texto do capítulo.",
            }
        )
        self.assertIn("# Sumário Executivo", md)
        self.assertIn("Texto do capítulo.", md)

    def test_newpage_directive(self) -> None:
        md = generate_markdown(
            {
                "chapter_number": 2,
                "title": "História",
                "content": "Corpo.",
                "newpage": True,
            }
        )
        self.assertTrue(md.startswith("\\newpage"))

    def test_subtitle_block(self) -> None:
        md = generate_markdown(
            {
                "chapter_number": 3,
                "title": "Ciência",
                "content": "Corpo.",
                "subtitle": "Evidência revista por pares",
            }
        )
        self.assertIn("> **Evidência revista por pares**", md)

    def test_sections_instead_of_flat_content(self) -> None:
        md = generate_markdown(
            {
                "chapter_number": 4,
                "title": "Saúde",
                "content": "",
                "sections": [
                    {
                        "heading": "Cardiovascular",
                        "body": "Risco reduzido.",
                        "level": 1,
                    },
                    {
                        "heading": "Saúde mental",
                        "body": "Sem evidência de dano.",
                        "level": 2,
                    },
                ],
            }
        )
        self.assertIn("## Cardiovascular", md)
        self.assertIn("### Saúde mental", md)
        self.assertIn("Risco reduzido.", md)

    def test_citations_appendix(self) -> None:
        md = generate_markdown(
            {
                "chapter_number": 5,
                "title": "Segurança",
                "content": "Corpo.",
                "citations": ["[@who2023]", "[@emcdda2022]"],
            }
        )
        self.assertIn("### Referências do capítulo", md)
        self.assertIn("- [@who2023]", md)
        self.assertIn("- [@emcdda2022]", md)
        self.assertIn("references.bib", md)

    def test_sanitizes_html_in_title(self) -> None:
        md = generate_markdown(
            {
                "chapter_number": 6,
                "title": "Título <script>alert(1)</script> Limpo",
                "content": "Corpo.",
            }
        )
        self.assertIn("# Título alert(1) Limpo", md)
        self.assertNotIn("<script>", md)


# ---------------------------------------------------------------------------
# process_submission
# ---------------------------------------------------------------------------

class TestProcessSubmission(unittest.TestCase):
    def test_happy_path(self) -> None:
        result = process_submission(
            {
                "chapter_number": 1,
                "title": "Sumário Executivo",
                "content": "Texto introdutório.",
                "newpage": True,
            }
        )
        self.assertEqual(result["chapter_number"], 1)
        self.assertIn("# Sumário Executivo", result["markdown"])
        self.assertTrue(result["markdown"].startswith("\\newpage"))

    def test_validation_error_propagates(self) -> None:
        with self.assertRaises(ValidationError):
            process_submission({"chapter_number": "bad"})

    def test_sanitizes_title_in_result(self) -> None:
        result = process_submission(
            {
                "chapter_number": 2,
                "title": "Título <em>Realce</em>",
                "content": "Corpo.",
            }
        )
        self.assertEqual(result["title"], "Título Realce")


# ---------------------------------------------------------------------------
# Integration / edge cases
# ---------------------------------------------------------------------------

class TestIntegration(unittest.TestCase):
    def test_full_realistic_submission(self) -> None:
        """Simulates a realistic submission for the repo."""
        result = process_submission(
            {
                "chapter_number": 3,
                "title": "Evidência Científica",
                "subtitle": "Revisão da literatura",
                "content": "",
                "newpage": True,
                "sections": [
                    {
                        "heading": "Metodologia",
                        "body": "Este capítulo baseia-se em revisão sistemática. "
                        "As fontes primárias incluem [@who2023] e [@emcdda2022].",
                        "level": 1,
                    },
                    {
                        "heading": "Resultados",
                        "body": "A evidência aponta para redução de danos.",
                        "level": 1,
                    },
                ],
                "citations": ["[@who2023]", "[@emcdda2022]", "[@hall2019]"],
            }
        )
        self.assertEqual(result["chapter_number"], 3)
        md = result["markdown"]
        self.assertTrue(md.startswith("\\newpage"))
        self.assertIn("# Evidência Científica", md)
        self.assertIn("> **Revisão da literatura**", md)
        self.assertIn("## Metodologia", md)
        self.assertIn("[@who2023]", md)
        self.assertIn("[@emcdda2022]", md)
        self.assertIn("### Referências do capítulo", md)
        self.assertIn("- [@hall2019]", md)

    def test_empty_sections_list(self) -> None:
        """Content is empty and sections list is empty — should validate fine
        but markdown won't have much body."""
        result = process_submission(
            {
                "chapter_number": 7,
                "title": "Vazio",
                "content": "Still valid because content is non-empty.",
                "sections": [],
            }
        )
        self.assertIn("# Vazio", result["markdown"])


class TestEdgeCases(unittest.TestCase):
    def test_title_with_special_chars(self) -> None:
        result = process_submission(
            {
                "chapter_number": 8,
                "title": "Portugal & Europa: 2001–2024",
                "content": "Dados.",
            }
        )
        self.assertIn("# Portugal & Europa: 2001–2024", result["markdown"])

    def test_citation_colon_syntax(self) -> None:
        """Repo uses [@citekey:value] format in some places."""
        validate_submission(
            {
                "chapter_number": 9,
                "title": "Teste",
                "content": "Corpo.",
                "citations": ["[@foo:42]", "[@bar:p123]"],
            }
        )

    def test_content_with_newpage_macro(self) -> None:
        """Content that already contains LaTeX macros should pass through."""
        result = process_submission(
            {
                "chapter_number": 10,
                "title": "Macro Test",
                "content": r"\newpage\section{Intro}",
            }
        )
        self.assertIn(r"\newpage\section{Intro}", result["markdown"])


if __name__ == "__main__":
    unittest.main()
