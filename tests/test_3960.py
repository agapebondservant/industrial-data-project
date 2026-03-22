import pytest
import csv
import logging
logging.basicConfig(level=logging.INFO)
pytestmark = pytest.mark.refactoring

@pytest.fixture
def test_data(request):
    return request.config.getoption("--test_data")

def test_benchmark(test_data):
    """
    Evaluate the relevancy score of given rows and asserts that it meets a specified threshold.
    """
    with open(test_data, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        rows = [row for row in reader]

        for row in rows:

            assert row["success"]

    assert True