# Live preview updates

After editing `activation-journey.html`, run `python3 scripts/update_preview_version.py` before committing. Include both the HTML and `preview-version.json` in the commit. The live preview polls the small version file and downloads the HTML only when its revision changes.

Use this stable preview URL for the user:
https://htmlpreview.github.io/?https://github.com/sorooshkln/test/blob/main/activation-journey.html?nikpos_live=2

Preserve the user's activation progress when updating the preview. Do not replace a main-branch link with a commit-specific link.
