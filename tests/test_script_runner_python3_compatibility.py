#!/usr/bin/env python3
"""
Unit tests for Python 3 compatibility in script_runner.py.
"""

import pytest
from src.automation.script_runner import ScriptRunner


def test_script_runner_initialization():
    """Test ScriptRunner initialization without print statements."""
    runner = ScriptRunner("/tmp")
    assert runner.script_directory == "/tmp"


def test_script_runner_load_script():
    """Test loading a script without print statements."""
    runner = ScriptRunner("/tmp")
    # Mock script content
    script_content = """
def test_function():
    return 42
"""

    # Mock open and write to avoid file operations
    with pytest.raises(FileNotFoundError):
        runner.load_script("/tmp/nonexistent_script.py")


def test_script_runner_exception_handling():
    """Test exception handling in ScriptRunner."""
    runner = ScriptRunner("/tmp")

    # Mock exception handling (Python 3 compatible)
    with pytest.raises(Exception) as exc_info:
        runner.execute_script("/tmp/nonexistent_script.py")

    assert "PlatformError" in str(exc_info.value) or "FileNotFoundError" in str(
        exc_info.value
    )
