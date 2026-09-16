"""Regression tests for the static validator only."""
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        self.skill = self.root / 'skills/hybrid-teach/SKILL.md'

    def run_check(self, optimized=False):
        flags = ['-O'] if optimized else []
        return subprocess.run([sys.executable, *flags, str(self.root / 'scripts/check.py')],
                              capture_output=True, text=True)

    def test_valid_package(self):
        self.assertEqual(self.run_check().returncode, 0)

    def test_invalid_name_under_both_modes(self):
        self.skill.write_text(self.skill.read_text().replace('name: hybrid-teach', 'name: INVALID NAME'))
        for mode in (False, True):
            with self.subTest(optimized=mode):
                result = self.run_check(mode)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('Invalid skill name', result.stderr)

    def test_missing_description(self):
        self.skill.write_text('\n'.join(line for line in self.skill.read_text().splitlines()
                                        if not line.startswith('description:')))
        self.assertNotEqual(self.run_check().returncode, 0)

    def test_malformed_frontmatter(self):
        self.skill.write_text('no metadata\n')
        self.assertNotEqual(self.run_check().returncode, 0)

    def test_broken_reference(self):
        with self.skill.open('a') as file:
            file.write('\n[missing](references/missing.md)\n')
        self.assertNotEqual(self.run_check().returncode, 0)

    def test_missing_license(self):
        (self.root / 'LICENSE').unlink()
        self.assertNotEqual(self.run_check().returncode, 0)

    def test_duplicate_metadata(self):
        self.skill.write_text(self.skill.read_text().replace('name: hybrid-teach',
                                                           'name: hybrid-teach\nname: hybrid-teach'))
        self.assertNotEqual(self.run_check().returncode, 0)


if __name__ == '__main__':
    unittest.main()
