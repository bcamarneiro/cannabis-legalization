import os
import re
import shutil
import subprocess
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent
SITE = PROJECT / "output" / "site"


def pandoc_major():
    if not shutil.which("pandoc"):
        return 0
    out = subprocess.run(["pandoc", "--version"], capture_output=True, text=True).stdout
    return int(re.search(r"pandoc (\d+)", out).group(1))


@unittest.skipUnless(pandoc_major() >= 3, "precisa de pandoc 3.x")
class SiteBuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        SITE.mkdir(parents=True, exist_ok=True)
        (SITE / "stale.html").write_text("obsoleto", encoding="utf-8")
        env = dict(os.environ, SKIP_PAGEFIND="1")
        subprocess.run(["bash", str(PROJECT / "scripts" / "build-site.sh")], check=True, env=env, cwd=PROJECT)
        cls.pages = sorted(SITE.glob("*.html"))

    def test_stale_pages_are_removed(self):
        self.assertFalse((SITE / "stale.html").exists())

    def test_one_page_per_chapter_plus_index(self):
        self.assertTrue((SITE / "index.html").exists())
        self.assertGreaterEqual(len(self.pages), 17)

    def test_citations_are_resolved(self):
        for page in self.pages:
            self.assertNotIn("[@", page.read_text(encoding="utf-8"), page.name)

    def test_every_page_is_searchable_and_styled(self):
        for page in self.pages:
            html = page.read_text(encoding="utf-8")
            self.assertIn("data-pagefind-body", html, page.name)
            self.assertIn('href="site.css"', html, page.name)
        self.assertTrue((SITE / "site.css").exists())

    def test_version_is_shown(self):
        version = (PROJECT / "VERSION").read_text().strip()
        self.assertIn(version, (SITE / "index.html").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
