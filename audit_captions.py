#!/usr/bin/env python3
"""
Image Caption Audit Script
===========================
Reads readme.md and audits all photo captions for:
  - Year
  - Location
  - Copyright / photographer credit (© symbol or "Photo:")

Run this after restructure_repo.py and after all new images have been added.

Usage:
    python3 audit_captions.py

Run from inside the Circuitry-Based-Sound repository root.

Output:
    - Console report
    - audit_captions_report.md (for reference while fixing)
"""

import re
from pathlib import Path


# ============================================================
# CONFIGURATION
# ============================================================

README_FILE = "readme.md"
REPORT_FILE = "audit_captions_report.md"

# File extensions to audit (photos only, not SVGs)
PHOTO_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}

# Skip these image paths (e.g. diagrams that look like photos)
SKIP_PATTERNS = [
    'waveform',
    'schematic',
    'diagram',
    'breadboard',
    'pinout',
    'overlay',
    'board',
    'revision',
    'deadlock',
]

# Patterns that indicate a year is present (4-digit number 1900-2099)
YEAR_PATTERN = re.compile(r'\b(19|20)\d{2}\b')

# Patterns that indicate a copyright credit is present
COPYRIGHT_PATTERN = re.compile(r'(©|\(c\)|Photo:|photo:|Foto:|foto:|Image:)', re.IGNORECASE)

# Known locations — extend this list as needed
KNOWN_LOCATIONS = [
    'ZKM', 'Karlsruhe', 'Langa', 'Cape Town', 'Khwa', 'Kinemathek',
    'Berlin', 'London', 'Tokyo', 'HfG', 'München', 'Munich',
]

# ============================================================
# HELPERS
# ============================================================

def is_photo(filename: str) -> bool:
    """Return True if file is a photo (not SVG or other graphic)."""
    ext = Path(filename).suffix.lower()
    if ext not in PHOTO_EXTENSIONS:
        return False
    name_lower = filename.lower()
    for pattern in SKIP_PATTERNS:
        if pattern in name_lower:
            return False
    return True


def extract_caption(content: str, img_ref: str) -> str:
    """
    Extract the caption that follows an image reference in the README.
    Handles both markdown image syntax and HTML img tags.
    Captions are typically on the next non-empty line, often in italics (*caption*).
    """
    # Escape special regex chars in the reference
    escaped = re.escape(img_ref)

    # Find position of the image reference
    match = re.search(escaped, content)
    if not match:
        return ""

    # Get text after the image reference
    after = content[match.end():]

    # Look for caption on the next lines (skip blank lines, HTML tags)
    lines = after.split('\n')
    for line in lines[:5]:  # Check up to 5 lines ahead
        stripped = line.strip()
        if not stripped:
            continue
        # Skip HTML tags and markdown directives
        if stripped.startswith('<') or stripped.startswith('[') or stripped.startswith('#'):
            continue
        # Found a caption candidate
        # Remove italic markers
        caption = stripped.strip('*').strip()
        if caption:
            return caption
    return ""


def check_year(caption: str) -> bool:
    return bool(YEAR_PATTERN.search(caption))


def check_location(caption: str) -> bool:
    for loc in KNOWN_LOCATIONS:
        if loc.lower() in caption.lower():
            return True
    return False


def check_copyright(caption: str) -> bool:
    return bool(COPYRIGHT_PATTERN.search(caption))


def find_all_images(content: str) -> list[tuple[str, str]]:
    """
    Find all image references in readme.md.
    Returns list of (reference_string, filename) tuples.
    """
    results = []

    # Markdown images: ![alt](path)
    for match in re.finditer(r'!\[.*?\]\(([^)]+)\)', content):
        path = match.group(1)
        filename = Path(path).name
        results.append((path, filename))

    # HTML img src=
    for match in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE):
        path = match.group(1)
        filename = Path(path).name
        results.append((path, filename))

    # HTML source srcset= (skip — these are SVG light/dark variants)
    # Not included intentionally

    return results


# ============================================================
# MAIN
# ============================================================

def main():
    repo_root = Path(__file__).parent
    readme_path = repo_root / README_FILE

    if not readme_path.exists():
        print(f"❌ {README_FILE} not found in {repo_root}")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("=" * 60)
    print("IMAGE CAPTION AUDIT")
    print("=" * 60)

    all_images = find_all_images(content)
    photos = [(ref, name) for ref, name in all_images if is_photo(name)]

    print(f"\nFound {len(all_images)} total image references")
    print(f"Auditing {len(photos)} photo(s) (SVGs and diagrams excluded)\n")
    print("=" * 60)

    # Track results
    ok = []
    warnings = []
    errors = []

    report_lines = [
        "# Image Caption Audit Report\n",
        f"Generated from `{README_FILE}`\n",
        "---\n",
    ]

    for ref, filename in photos:
        caption = extract_caption(content, ref)

        has_year = check_year(caption)
        has_location = check_location(caption)
        has_credit = check_copyright(caption)

        missing = []
        if not has_year:
            missing.append("year")
        if not has_location:
            missing.append("location")
        if not has_credit:
            missing.append("© credit")

        # Determine status
        if not missing:
            status = "✅"
            ok.append(filename)
        elif len(missing) == 3:
            status = "❌"
            errors.append(filename)
        else:
            status = "⚠️ "
            warnings.append(filename)

        # Console output
        print(f"{status} {filename}")
        if caption:
            print(f"   Caption: \"{caption}\"")
        else:
            print(f"   Caption: (none found)")
        print(f"   Year: {'✅' if has_year else '❌ missing'}  "
              f"Location: {'✅' if has_location else '❌ missing'}  "
              f"Credit: {'✅' if has_credit else '❌ missing'}")
        if missing:
            print(f"   → Add: {', '.join(missing)}")
        print()

        # Report lines
        report_lines.append(f"## {status} `{filename}`\n")
        report_lines.append(f"**Caption:** {caption if caption else '*(none found)*'}\n\n")
        report_lines.append(f"- Year: {'✅' if has_year else '❌ missing'}\n")
        report_lines.append(f"- Location: {'✅' if has_location else '❌ missing'}\n")
        report_lines.append(f"- Copyright credit: {'✅' if has_credit else '❌ missing'}\n")
        if missing:
            report_lines.append(f"\n**Action required:** Add {', '.join(missing)}\n")
        report_lines.append("\n**Suggested format:**\n")
        report_lines.append(
            f"```\n*[Description]. [Location], [Year]. © [Photographer]*\n```\n\n"
        )
        report_lines.append("---\n\n")

    # Summary
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  ✅ Complete:          {len(ok)}")
    print(f"  ⚠️  Partially missing: {len(warnings)}")
    print(f"  ❌ Fully missing:     {len(errors)}")
    print(f"  Total photos audited: {len(photos)}")
    print("=" * 60)

    # Write report file
    report_path = repo_root / REPORT_FILE
    with open(report_path, 'w', encoding='utf-8') as f:
        f.writelines(report_lines)

    print(f"\n📄 Full report written to: {REPORT_FILE}")
    print("   Use this file as a checklist while fixing captions in readme.md")


if __name__ == "__main__":
    main()
