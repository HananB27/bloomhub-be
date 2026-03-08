#!/usr/bin/env python3
"""
Validate .cm (gitStream) config files before commit.
Catches YAML and basic structure errors. Expression syntax is validated by gitStream in CI.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "validate_gitstream_cm: install PyYAML (e.g. pip install pyyaml) for validation",
        file=sys.stderr,
    )
    sys.exit(0)


def validate(path: Path) -> list[str]:
    errors = []
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        errors.append(f"{path}: Invalid YAML - {e}")
        return errors
    if not data:
        errors.append(f"{path}: File is empty or invalid")
        return errors
    if "manifest" not in data:
        errors.append(f"{path}: Missing required 'manifest' section")
    if "automations" not in data and "has" not in data:
        errors.append(f"{path}: Missing 'automations' or 'has' section")
    return errors


def main() -> int:
    if len(sys.argv) < 2:
        return 0
    all_errors = []
    for p in sys.argv[1:]:
        path = Path(p)
        if path.suffix != ".cm" or not path.exists():
            continue
        all_errors.extend(validate(path))
    if all_errors:
        for e in all_errors:
            print(e, file=sys.stderr)
        print(
            "\nFor full expression validation, use https://app.gitstream.cm/playground",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
