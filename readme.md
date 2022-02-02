# Trying Out PyTest

This repository is a first trial of PyTest. It is primarily designed for **Unit Tests**. I'm following this video: https://www.youtube.com/watch?v=byaxg00Gf9I

# Prerequisites
Install the PyTest package by running `pip install -U pytest`

# Test file naming rules
Files containing tests must be named `test_+.py`or `*_test.py`in order to be recognized by PyTest as such kind of files.

# Test creation
The test file has to first of all `import pytest`. Tests are written as a function named `test_*`. Use Python's `assert` command to define the expected outcome of a test. An assert comes back either _true_ or _false_ and hence indicates whether a test passed or not. As an example, see "first_test.py". Tests can be labeled using `@pytest.mark.$name`

# Execution
All test files in the current directory can be run with `pytest` or an individual test file by `pytest first_test.py`. The "marked" tests can be run via `pytest -m $name`. Verbose mode can be enabled by adding `-v` to the execution command.

# Fixtures
Fixtures is code that runs before a test is executed. The code written after `@pytest.fixture` is run before _each_ of the following tests. In "test_withFixture.py" an array of numbers is defined beforehand.

# Parametrized Tests
Tests that essentially use a "table" of data from where to grab multiple input values to go through multiple test runs.

# Skip
Skip a test by writing `@pytest.mark.skip`above the test that's supposed to be skipped. Skipping a test that's known to fail, use `@pytest.mark.xfail` instead.

