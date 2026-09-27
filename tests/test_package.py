"""Offline package integrity only; these tests do not measure agent behavior."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageIntegrity(unittest.TestCase):
    def test_single_entrypoint(self):
        self.assertEqual([p.relative_to(ROOT).as_posix() for p in ROOT.rglob('SKILL.md') if '.git' not in p.parts], ['SKILL.md'])

    def test_identity(self):
        manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(manifest['name'], 'step-back')
        self.assertIn('name: step-back', (ROOT / 'SKILL.md').read_text(encoding='utf-8'))
        self.assertRegex(manifest['version'], r'^\d+\.\d+\.\d+$')

    def test_local_markdown_links(self):
        for file in ROOT.rglob('*.md'):
            for link in re.findall(r'\]\(([^)]+)\)', file.read_text(encoding='utf-8')):
                if '://' in link or link.startswith('#'):
                    continue
                self.assertTrue((file.parent / link.split('#')[0]).is_file(), (str(file), link))

    def test_notice_and_license(self):
        self.assertIn('MIT License', (ROOT / 'LICENSE').read_text(encoding='utf-8'))
        notices = (ROOT / 'THIRD_PARTY_NOTICES.md').read_text(encoding='utf-8')
        for author in ['2026 555cider', '2026 Jet Xu']:
            self.assertIn(author, notices)


if __name__ == '__main__':
    unittest.main()
