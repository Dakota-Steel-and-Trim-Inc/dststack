import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("compare_installation.py")


class CompareInstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.installed = self.root / "installed"
        self.skill = self.source / "example"
        (self.skill / "references").mkdir(parents=True)
        (self.skill / "SKILL.md").write_text("example instructions")
        (self.skill / "references" / "guide.md").write_text("original reference")
        shutil.copytree(self.source, self.installed)
        self.lock = self.root / ".skill-lock.json"
        self.write_lock("git@github.com:Dakota-Steel-and-Trim-Inc/dststack.git")

    def write_lock(self, source):
        self.lock.write_text(json.dumps({"skills": {"example": {"source": source}}}))

    def run_comparison(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--source-dir", str(self.source),
             "--installed-dir", str(self.installed), "--lock-file", str(self.lock), "--json"],
            capture_output=True, text=True,
        )

    def test_matching_directory_and_supported_root_symlink_are_read_only(self):
        target = self.root / "shared-example"
        (self.installed / "example").rename(target)
        (self.installed / "example").symlink_to(target, target_is_directory=True)
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        result = self.run_comparison()
        self.assertEqual(result.returncode, 0, result.stderr)
        record = json.loads(result.stdout)["skills"][0]
        self.assertEqual((record["content"], record["provenance"]), ("match", "match"))
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_reference_changes_missing_files_and_extra_files(self):
        skill = self.installed / "example"
        (skill / "references" / "guide.md").write_text("changed reference")
        (skill / "SKILL.md").unlink()
        (skill / "extra.md").write_text("extra content")
        (skill / ".DS_Store").write_text("ignored OS metadata")
        result = self.run_comparison()
        self.assertEqual(result.returncode, 1, result.stderr)
        record = json.loads(result.stdout)["skills"][0]
        self.assertEqual(record["changed"], ["references/guide.md"])
        self.assertEqual(record["missing"], ["SKILL.md"])
        self.assertEqual(record["extra"], ["extra.md"])

    def test_provenance_mismatch_and_unknown_do_not_report_success(self):
        for source in ["mattpocock/skills", "https://user:secret@example.com/private"]:
            with self.subTest(source=source):
                self.write_lock(source)
                result = self.run_comparison()
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertNotIn("secret", result.stdout + result.stderr)
                self.assertEqual(json.loads(result.stdout)["skills"][0]["provenance"], "different")
        self.lock.unlink()
        result = self.run_comparison()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(json.loads(result.stdout)["skills"][0]["provenance"], "unknown")

    def test_missing_skill_is_reported_without_creating_it(self):
        shutil.rmtree(self.installed / "example")
        result = self.run_comparison()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(json.loads(result.stdout)["skills"][0]["content"], "missing")
        self.assertFalse((self.installed / "example").exists())

    def test_invalid_inputs_fail_instead_of_looking_clean(self):
        for value in ["not json", "[]", '{"skills": []}']:
            with self.subTest(value=value):
                self.lock.write_text(value)
                result = self.run_comparison()
                self.assertEqual(result.returncode, 2)
        self.write_lock("Dakota-Steel-and-Trim-Inc/dststack")
        shutil.rmtree(self.source)
        result = self.run_comparison()
        self.assertEqual(result.returncode, 2)

    def test_nested_directory_links_cannot_hide_uncounted_content(self):
        external = self.root / "external"
        external.mkdir()
        (external / "private.txt").write_text("do not print this")
        (self.installed / "example" / "linked").symlink_to(external, target_is_directory=True)
        result = self.run_comparison()
        self.assertEqual(result.returncode, 2)
        self.assertNotIn("do not print this", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
