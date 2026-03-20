import csv
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--test_data",
        action="store",
        default="./temp/test_data.csv",
        help='Specify test data file path.'
    )
    parser.addoption(
        "--test_results",
        action="store",
        default="./temp/test_results.csv",
        help='Specify test results file path.'
    )


def pytest_configure(config):
    config._test_results = []
    config.addinivalue_line("markers", "refactoring: mark test as target for refactoring.")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()

    if report.when == 'call' or report.failed:

        item.config._test_results.append({
            "name": item.nodeid,
            "outcome": report.outcome.upper(),
            "error": report.longreprtext if report.failed else ""
        })

def pytest_sessionfinish(session, exitstatus):
    results = session.config._test_results

    if not results:

        return

    keys = results[0].keys()

    test_results_path = session.config.getoption("--test_results")

    with open(test_results_path, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=keys)

        writer.writeheader()

        writer.writerows(results)
