#!/usr/bin/env python3
"""Static packaging checks, not a model-behavior or learning-effectiveness test."""
from pathlib import Path
import re
import sys


def validate(root):
    errors = []
    skill = root / 'skills/hybrid-teach/SKILL.md'
    if not skill.is_file():
        return ['Missing SKILL.md']
    text = skill.read_text()
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    fields = {}
    if not match:
        errors.append('Missing or malformed frontmatter')
    else:
        for line in match.group(1).splitlines():
            if ': ' not in line:
                errors.append('Unsupported metadata line: ' + line)
                continue
            key, value = line.split(': ', 1)
            if key in fields:
                errors.append('Duplicate metadata: ' + key)
            fields[key] = value.strip()
    name = fields.get('name', '')
    if name != skill.parent.name or len(name) > 64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
        errors.append('Invalid skill name')
    if not 0 < len(fields.get('description', '')) <= 1024:
        errors.append('Missing or invalid description')
    for md in root.rglob('*.md'):
        if '.git' in md.relative_to(root).parts:
            continue
        for link in re.findall(r'\]\(([^)]+)\)', md.read_text()):
            if '://' not in link and not link.startswith('#'):
                if not (md.parent / link.split('#')[0]).is_file():
                    errors.append(f'Broken local link: {md.relative_to(root)} -> {link}')
    for required in ('LICENSE', 'README.md', 'skills/hybrid-teach/references/state.md',
                     'skills/hybrid-teach/references/assessment.md'):
        if not (root / required).is_file():
            errors.append('Missing required file: ' + required)
    return errors


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print('\n'.join('FAIL: ' + e for e in errors), file=sys.stderr)
        return 1
    print('PASS: metadata, local links, required files')
    print('Model behavior and learning effectiveness are NOT tested here.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
