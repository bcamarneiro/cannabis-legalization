import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

LUA = Path(__file__).resolve().parent.parent / "site" / "section-actions.lua"


@unittest.skipUnless(shutil.which("pandoc"), "pandoc não instalado")
class SectionActionsTest(unittest.TestCase):
    def render(self, md, sectionmap):
        meta = Path(tempfile.mkdtemp()) / "meta.json"
        meta.write_text(json.dumps({"repo": "dono/repo", "sectionmap": sectionmap}), encoding="utf-8")
        return subprocess.run(
            ["pandoc", "--from", "markdown", "--to", "html", "--lua-filter", str(LUA), "--metadata-file", str(meta)],
            input=md, capture_output=True, text=True, check=True,
        ).stdout

    def test_links_are_added_under_the_heading(self):
        html = self.render("## Riscos {#riscos}\n\ntexto\n", {"riscos": "chapters/02-ciencia.md"})
        self.assertIn('class="section-actions"', html)
        self.assertIn('href="#riscos"', html)
        self.assertIn("https://github.com/dono/repo/issues/new?template=propor-alteracao.yml&section=riscos", html)
        self.assertIn("https://github.com/dono/repo/edit/main/chapters/02-ciencia.md", html)

    def test_ids_with_accents_and_dots_are_percent_encoded(self):
        html = self.render(
            "## Estratégia {#5.5-estratégia-de-negociação}\n",
            {"5.5-estratégia-de-negociação": "chapters/10-politica.md"},
        )
        self.assertIn("section=5.5-estrat%C3%A9gia-de-negocia%C3%A7%C3%A3o", html)
        self.assertNotIn("section=5.5-estratégia", html)

    def test_level4_and_headings_without_map_entry_get_no_edit_link(self):
        html = self.render("#### Detalhe {#detalhe}\n\n## Sem mapa {#sem-mapa}\n", {})
        self.assertNotIn("section-actions", html.split("Sem mapa")[0])
        self.assertIn("section=sem-mapa", html)
        self.assertNotIn("/edit/main/", html)


if __name__ == "__main__":
    unittest.main()
