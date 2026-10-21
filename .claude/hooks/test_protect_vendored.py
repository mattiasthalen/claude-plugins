import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import protect_vendored  # noqa: E402


class ProtectVendored(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        (self.root / "scripts").mkdir()
        (self.root / "scripts" / "vendor.json").write_text(json.dumps({"copies": [{"dest": "plugins/sdlc/skills/pr"}]}))

    def decide(self, path):
        return protect_vendored.decide({"cwd": str(self.root), "tool_input": {"file_path": path}}, self.root)

    def test_refuses_vendored_files(self):
        self.assertIsNotNone(self.decide("plugins/sdlc/skills/pr/SKILL.md"))
        self.assertIsNotNone(self.decide(str(self.root / "plugins/sdlc/skills/pr/CREDITS.md")))

    def test_allows_vendored_note_and_elsewhere(self):
        self.assertIsNone(self.decide("plugins/sdlc/skills/pr/VENDORED.md"))
        self.assertIsNone(self.decide("plugins/sdlc/skills/sdlc/SKILL.md"))
        self.assertIsNone(self.decide("plugins/sdlc/skills/prx/SKILL.md"))

    def test_no_manifest_allows(self):
        (self.root / "scripts" / "vendor.json").unlink()
        self.assertIsNone(self.decide("plugins/sdlc/skills/pr/SKILL.md"))


if __name__ == "__main__":
    unittest.main()
