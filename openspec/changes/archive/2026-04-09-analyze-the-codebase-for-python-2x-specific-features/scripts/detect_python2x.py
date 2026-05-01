#!/usr/bin/env python3
"""
Script to detect Python 2x-specific syntax and dependencies in the codebase.
"""

import os
import re
import subprocess
from pathlib import Path

# Patterns for Python 2x-specific syntax
PYTHON2X_PATTERNS = {
    "print_statements": r"print\s+.*",
    "except_syntax": r"except\s+.*,\s*.*:",
    "division_behavior": r"\b\d+/\d+\b",  # Simple integer division
    "python2_imports": r"from\s+.*\s+import\s+.*",  # Detect Python 2x-only libraries
}


def scan_directory(directory):
    """Scan a directory for Python 2x-specific syntax."""
    findings = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                for pattern_type, pattern in PYTHON2X_PATTERNS.items():
                    matches = re.findall(pattern, content)
                    if matches:
                        findings.append(
                            {
                                "file": file_path,
                                "pattern": pattern_type,
                                "matches": matches[:3],  # Limit to 3 examples
                            }
                        )

    return findings


def generate_report(findings, output_file="python2x_report.md"):
    """Generate a Markdown report of findings."""
    with open(output_file, "w") as f:
        f.write("# Python 2x-Specific Syntax Report\n\n")
        f.write("## Findings\n")

        for finding in findings:
            f.write(f"### File: {finding['file']}\n")
            f.write(f"#### Pattern: {finding['pattern']}\n")
            f.write(f"#### Matches:\n")
            for match in finding["matches"]:
                f.write(f"- {match}\n")
            f.write("\n")

    print(f"Report generated: {output_file}")


def main():
    """Main function to execute the scan."""
    directory = (
        "/opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp"
    )
    findings = scan_directory(directory)
    generate_report(findings)


if __name__ == "__main__":
    main()
