#!/usr/bin/env python3
"""
Script to validate Python 3 compatibility for refactored components.
"""

import os
import re
import subprocess
from pathlib import Path


def run_2to3_check(file_path):
    """Run 2to3 to check for Python 2x-specific syntax."""
    try:
        result = subprocess.run(
            ["2to3", "-n", "-w", "--no-diffs", file_path],
            capture_output=True,
            text=True,
            check=True,
        )
        return True, "2to3 check passed"
    except subprocess.CalledProcessError as e:
        return False, f"2to3 check failed: {e.stderr}"


def run_pylint_check(file_path):
    """Run pylint to enforce Python 3 compliance."""
    try:
        result = subprocess.run(
            [
                "pylint",
                "--disable=all",
                "--enable=old-style-class,old-raise,syntax-error",
                file_path,
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        return True, "Pylint check passed"
    except subprocess.CalledProcessError as e:
        return False, f"Pylint check failed: {e.stderr}"


def check_python3_compatibility(file_path):
    """Check Python 3 compatibility for a single file."""
    print(f"Checking {file_path}...")

    # Check for Python 2x-specific syntax
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    python2x_patterns = {
        "print_statements": r"print\s+.*",
        "except_syntax": r"except\s+.*,\s*.*:",
        "division_behavior": r"\b\d+/\d+\b",
        "python2_imports": r"from\s+.*\s+import\s+.*",
    }

    issues = []
    for pattern_type, pattern in python2x_patterns.items():
        matches = re.findall(pattern, content)
        if matches:
            issues.append(f"{pattern_type}: {matches[:1]}")

    # Run 2to3 and pylint
    if issues:
        print(f"  Issues found: {', '.join(issues)}")
        return False, f"Python 2x issues detected: {issues}"

    # Run 2to3 check
    success, message = run_2to3_check(file_path)
    if not success:
        return False, message

    # Run pylint check
    success, message = run_pylint_check(file_path)
    if not success:
        return False, message

    return True, "Python 3 compatible"


def main():
    """Main function to execute compatibility checks."""
    directory = (
        "/opt/app-root/src/legacy-code-agentmesh/workflows/1_simple_code_generation/tmp"
    )

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                success, message = check_python3_compatibility(file_path)
                print(f"  Result: {message}")


if __name__ == "__main__":
    main()
