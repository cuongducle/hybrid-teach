#!/usr/bin/env python3
"""Dependency-free static packaging checks; not a tutoring effectiveness test."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / 'skills/hybrid-teach/SKILL.md'
text = skill.read_text()
front = text.split('---', 2)[1]
fields = dict(line.split(': ', 1) for line in front.strip().splitlines())
assert fields['name'] == skill.parent.name
assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields['name'])
assert 0 < len(fields['description']) <= 1024
for md in root.rglob('*.md'):
    if '.git' in md.parts:
        continue
    for link in re.findall(r'\]\(([^)]+)\)', md.read_text()):
        if '://' not in link and not link.startswith('#'):
            assert (md.parent / link.split('#')[0]).exists(), (md, link)
for marker in ('5 diagnostic questions', 'independent attempt', 'explicit permission',
               'Do not manufacture universal truths', 'There are no automatic notifications',
               'LEARNER.md', 'REVIEW.md'):
    assert marker in text, marker
assert (root / 'LICENSE').exists()
print('PASS: metadata, local links, workflow safeguards, license')
print('Behavioral scenarios are manual and have not been executed by this check.')
