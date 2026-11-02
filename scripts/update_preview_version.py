#!/usr/bin/env python3
"""Update the small live-preview revision file after editing the standalone HTML."""
import hashlib
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent.parent
html_path = root / 'activation-journey.html'
html = html_path.read_text(encoding='utf-8')
pattern = r"const PREVIEW_VERSION='[^']*';"
if len(re.findall(pattern, html)) != 1:
    raise SystemExit('Expected exactly one live-preview version marker.')
canonical = re.sub(pattern, "const PREVIEW_VERSION='';", html)
version = hashlib.sha256(canonical.encode('utf-8')).hexdigest()
updated = re.sub(pattern, f"const PREVIEW_VERSION='{version}';", html)
if updated != html:
    html_path.write_text(updated, encoding='utf-8')
(root / 'preview-version.json').write_text(json.dumps({'version': version}) + '\n', encoding='utf-8')
print(version)
