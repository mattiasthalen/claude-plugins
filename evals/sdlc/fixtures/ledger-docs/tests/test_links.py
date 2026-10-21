import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\]\(([^)#]+)(?:#[^)]*)?\)")


class RelativeLinksTest(unittest.TestCase):
    def test_every_relative_link_resolves(self):
        pages = [ROOT / "README.md", *sorted((ROOT / "guide").glob("*.md"))]
        broken = []
        for page in pages:
            for target in LINK.findall(page.read_text(encoding="utf-8")):
                if "://" in target:
                    continue
                if not (page.parent / target).exists():
                    broken.append(f"{page.relative_to(ROOT)} -> {target}")
        self.assertEqual(broken, [])


if __name__ == "__main__":
    unittest.main()
