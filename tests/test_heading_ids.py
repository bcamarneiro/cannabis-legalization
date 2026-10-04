import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import heading_ids as hi  # noqa: E402


def make_chapters(files):
    root = Path(tempfile.mkdtemp())
    (root / "chapters").mkdir()
    for name, text in files.items():
        (root / "chapters" / name).write_text(text, encoding="utf-8")
    return root


class SlugifyTest(unittest.TestCase):
    def test_cases(self):
        cases = {
            "Impacto no consumo juvenil": "impacto-no-consumo-juvenil",
            "3.5 Impacto": "impacto",
            "Tailândia (2022–2026): o chicote político": "tailândia-20222026-o-chicote-político",
            "Idade 21 vs. Desenvolvimento — Transparência": "idade-21-vs.-desenvolvimento-transparência",
            "Autocultivo regulado *(proposta de compromisso)*": "autocultivo-regulado-proposta-de-compromisso",
            "[link](http://x.pt) texto": "link-texto",
            "2025": "section",
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(hi.slugify(text), expected)


class ScanAndAssignTest(unittest.TestCase):
    def test_fenced_code_is_ignored(self):
        root = make_chapters({"01-a.md": "# A\n\n```bash\n# comentário\n```\n"})
        headings, _, _ = hi.scan(root / "chapters")
        self.assertEqual([h.text for h in headings], ["A"])

    def test_attribute_block_without_id_is_rejected(self):
        root = make_chapters({"01-a.md": "# A {.unnumbered}\n"})
        with self.assertRaises(ValueError):
            hi.scan(root / "chapters")

    def test_duplicate_titles_get_distinct_stable_ids(self):
        root = make_chapters({"01-a.md": "# Riscos\n", "02-b.md": "# Riscos\n\n## Riscos\n"})
        headings, anchors, _ = hi.scan(root / "chapters")
        new = hi.assign_missing(headings, anchors)
        self.assertEqual([new[i] for i in sorted(new)], ["riscos", "riscos-1", "riscos-2"])

    def test_explicit_ids_are_kept_and_reserved(self):
        root = make_chapters({"01-a.md": "# Um {#riscos}\n\n## Riscos\n"})
        headings, anchors, _ = hi.scan(root / "chapters")
        new = hi.assign_missing(headings, anchors)
        self.assertEqual(list(new.values()), ["riscos-1"])

    def test_fix_is_idempotent(self):
        root = make_chapters({"01-a.md": "# A\n\n## B\n\ntexto\n"})
        hi.fix(root / "chapters")
        first = (root / "chapters" / "01-a.md").read_text(encoding="utf-8")
        self.assertEqual(first, "# A {#a}\n\n## B {#b}\n\ntexto\n")
        hi.fix(root / "chapters")
        self.assertEqual((root / "chapters" / "01-a.md").read_text(encoding="utf-8"), first)


class CheckTest(unittest.TestCase):
    def test_reports_missing_ids(self):
        root = make_chapters({"01-a.md": "# A\n"})
        problems = hi.check(root / "chapters", root / "no.lock")
        self.assertTrue(any("sem ID" in p for p in problems))

    def test_reports_duplicate_ids(self):
        root = make_chapters({"01-a.md": "# A {#x}\n\n## B {#x}\n"})
        problems = hi.check(root / "chapters", root / "no.lock")
        self.assertTrue(any("duplicado" in p for p in problems))

    def test_reports_broken_internal_links(self):
        root = make_chapters({"01-a.md": "# A {#a}\n\nVer [isto](#nao-existe) e [aquilo](#a).\n"})
        problems = hi.check(root / "chapters", root / "no.lock")
        self.assertEqual(len([p for p in problems if "quebrada" in p]), 1)
        self.assertTrue(any("#nao-existe" in p for p in problems))

    def test_link_to_level4_auto_id_is_valid(self):
        root = make_chapters({"01-a.md": "# A {#a}\n\n#### Detalhe fino\n\nVer [x](#detalhe-fino).\n"})
        self.assertEqual(hi.check(root / "chapters", root / "no.lock"), [])

    def test_locked_id_must_survive(self):
        root = make_chapters({"01-a.md": "# A {#novo}\n"})
        lock = root / "lock"
        lock.write_text("antigo\nnovo\n", encoding="utf-8")
        problems = hi.check(root / "chapters", lock)
        self.assertEqual(len([p for p in problems if "desapareceu" in p]), 1)

    def test_anchor_span_keeps_locked_id_alive(self):
        root = make_chapters({"01-a.md": '# A {#novo}\n<span id="antigo"></span>\n'})
        lock = root / "lock"
        lock.write_text("antigo\nnovo\n", encoding="utf-8")
        self.assertEqual(hi.check(root / "chapters", lock), [])


class MetaTest(unittest.TestCase):
    def test_sectionmap_points_to_chapter_files(self):
        root = make_chapters({"01-a.md": "# A {#a}\n", "02-b.md": "# B {#b}\n"})
        meta = hi.meta(root / "chapters", "dono/repo")
        self.assertEqual(meta["repo"], "dono/repo")
        self.assertEqual(meta["sectionmap"], {"a": "chapters/01-a.md", "b": "chapters/02-b.md"})


@unittest.skipUnless(shutil.which("pandoc"), "pandoc não instalado")
class PandocParityTest(unittest.TestCase):
    def test_slugs_match_pandoc_auto_identifiers(self):
        titles = [
            "Impacto no consumo juvenil",
            "Tailândia (2022–2026): o chicote político",
            "Idade 21 vs. Desenvolvimento — Transparência",
            "Autocultivo regulado *(proposta de compromisso)*",
            "3.5 Estratégia de Negociação em 3 Níveis",
        ]
        md = "\n\n".join(f"## {t}" for t in titles) + "\n"
        html = subprocess.run(
            ["pandoc", "--from", "markdown", "--to", "html"],
            input=md, capture_output=True, text=True, check=True,
        ).stdout
        pandoc_ids = re.findall(r'<h2 id="([^"]+)"', html)
        self.assertEqual(pandoc_ids, [hi.slugify(t) for t in titles])


if __name__ == "__main__":
    unittest.main()
