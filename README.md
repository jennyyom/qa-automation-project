# QA Automation Project

![Selenium Tests CI](https://github.com/jennyyom/qa-automation-project/actions/workflows/selenium-tests.yml/badge.svg)

A QA portfolio project that tests the login feature of
[The Internet](https://the-internet.herokuapp.com/login) demo site,
covering test planning, manual test case design, bug reporting,
and browser automation with Selenium and pytest.

## What's Included

| Area | Details |
|---|---|
| Test plan | `test-plan/test-plan.md` |
| Test cases | 15 documented cases (TC_001–TC_015) for login, session, and input validation |
| Automated tests | TC_001–TC_003 automated with Selenium WebDriver (Python) and pytest |
| Bug reports | Sample defect reports with steps to reproduce, expected and actual results |
| CI | GitHub Actions runs the automated tests on every push and pull request to `main` |

## Automated Tests

| ID | Scenario | Status |
|---|---|---|
| TC_001 | Valid login | Automated |
| TC_002 | Invalid password | Automated |
| TC_003 | Empty username | Automated |
| TC_004–TC_015 | See `test-cases/` | Documented, not yet automated |

The tests use explicit waits (`WebDriverWait`) instead of fixed sleeps,
and run in headless Chrome so they work the same locally and in CI.

## Tech Stack

- **Python** and **pytest**
- **Selenium WebDriver** with **webdriver-manager**
- **GitHub Actions** for continuous integration

## Project Structure

```
qa-automation-project/
├── .github/workflows/   # GitHub Actions CI
├── automation/
│   ├── tests/           # pytest test suite (run in CI)
│   └── scripts/         # earlier practice scripts
├── test-cases/          # manual test case documentation
├── test-plan/           # test plan
├── bug-reports/         # sample bug reports
├── docker/              # Docker setup (in progress)
└── requirements.txt
```

## How to Run

```bash
pip install -r requirements.txt
python -m pytest -v
```

## Roadmap

- [x] Replace fixed waits with explicit `WebDriverWait` conditions
- [x] Run tests in headless Chrome for CI
- [x] Run tests automatically with GitHub Actions
- [ ] Introduce the Page Object Model (`pages/`)
- [ ] Move shared fixtures to `conftest.py`
- [ ] Parametrize login tests and automate TC_004–TC_015
- [ ] Save a screenshot on failure and publish an HTML test report in CI
- [ ] Add API tests with `requests` and pytest
- [ ] Update the Docker setup to run the pytest suite
