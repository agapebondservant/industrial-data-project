import pytest
import logging
logging.basicConfig(level=logging.INFO)
pytestmark = pytest.mark.refactoring


def test_benchmark(row):
    """
    Evaluate the relevancy score of a single row and assert that it meets a specified threshold.
    Each row is parametrized by pytest_generate_tests in conftest.py, named by the row's 'name' field.
    """
    logging.info(f"Evaluating row: {row}...")
    assert row["success"]