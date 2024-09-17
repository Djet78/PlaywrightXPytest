[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[//]: # ([![pre-commit]&#40;https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&#41;]&#40;https://github.com/pre-commit/pre-commit&#41;)

# Playwright X Pytest X Allure
Playwright in combination with Pytest test framework, and <report_tool> retorting example.

#### Used python main packages:
1. `playwright` - Test runner.
4. `requrests` - API interactions. 
5. `poetry` - Dependencies management.
6. `ruff` - Linter and formatting tool.
7. `pytest` - for test management and execution. 

---

## Setup for Windows

### 1. Install Allure
1. Download Java 21: https://www.oracle.com/java/technologies/downloads/
2. Set `JAVA_HOME` environment variable, point it to the java root folder.
3. Download and unpack latest allure release: https://github.com/allure-framework/allure2/releases
4. Or using Scoop: https://allurereport.org/docs/gettingstarted-installation/#install-via-scoop-for-windows
5. Into `PATH` - add path to the allure.bat file. Ex: `*\allure\allure-2.24.1\bin`


### 2. Install Poetry
1. Install pipx via pip - https://github.com/pypa/pipx?tab=readme-ov-file
2. Install poetry via pipx - https://python-poetry.org/docs/#installing-with-pipx 
3. Add poetry executable into `PATH`. Ex: `c:\users\test\.local\bin`


### 3. Configure local project: 
1. Clone the repo
2. In the project root dir - run `poetry install`
3. Activate created env: `.\.venv\Scripts\activate`
4. Apply pre-commit hooks: `pre-commit install`
5. Install webdrivers `playwright install`


---


## Usage

All commands should be executed inside virtualenv, or be prefixed with `poetry run`

Execute tests
1. `pytest` - Run everything that project have.
2. `pytest -m "<scope>"` - Run all tests that marked by <scope>.
3. `pytest -m "<scope>" --browser <driver>` - Run all marked tests on mentioned driver.
4. `pytest --browser <driver>` - Run tests on a specified driver.
5. `pytest --browser <driver_1> --browser <driver_2>` - Run tests on all mentioned drivers.
6. `pytest --numprocesses 2` - Run tests in parallel. Recommend to use no more than half of logical CPU cores.
7. `pytest --slowmo 3000` - Adds a ms delay between webdriver actions. 
8. `pytest --device="Galaxy S III"` - Emulate devices settings and orientation. List of devices: https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json
9. `pytest -m "<scope>"` - Run all tests that marked by <scope>.
10. `pytest -c "<path_to_config_file.ini>"` - Execute tests with specific conf file. `pytest.ini` by default.

Generate reports
`allure serve allure-results` - Launch allure result on local server. Uses `allure-results` folder for report.
`allure generate` - Generate HTML report, based on results from `allure-results` folder.
`allure open` - open HTML report from `allure-report` folder.

Playwright
1. `playwright codegen <url>` - start tests recording tool on specified web page's url.
2. `playwright show-trace <full_file_path>` - see a test trace and debug it. 


## TODO
 
1. Add some sample tests using Playwright
   2. For API: https://playwright.dev/python/docs/api-testing
2. Find reporting tools for playwright
   2. Allure (using allure-pytest) - https://github.com/microsoft/playwright-python/issues/1265
   3. Lambdatest (Seems it have a freemium plan)- https://www.lambdatest.com/support/docs/pytest-on-hyperexecute/
   3. Report portal:
      4. https://github.com/reportportal/client-Python
      5. https://github.com/reportportal/agent-python-pytest
      5. https://pypi.org/project/pytest-reportportal/
   6. Squadcast (?) : https://pypi.org/project/pytest-squadcast/
   7. Calipe PRO: 
      8. https://app.calliope.pro/users/8401/dashboard
      9. https://docs.calliope.pro/supported-tools/pytest/
   7. Uploader to remote servers (Allure, pytest's html reports): https://pypi.org/project/pytest-upload-report/
   10. Katalon TestOps - Has a free plan, and Manual tests management:
       11. https://katalon.com/pricing
       12. https://docs.katalon.com/docs/katalon-platform/analyze/reports/upload-test-reports/upload-reports-from-other-framework/upload-test-reports-from-pytest-to-katalon-testops
   8. Zebrunner:
      9. Manual and Automation tool, have a free plan: https://zebrunner.com/testing-platform
      10. https://pypi.org/project/pytest-zebrunner/
   11. JSON (maybe for exporting into other formats) - https://pypi.org/project/pytest-json-report/

[//]: # (3. Configure CI/CD for app, using GitHub actions: https://playwright.dev/python/docs/ci#github-actions)
[//]: # (   4. Trace recording could be useful for CI: https://playwright.dev/python/docs/trace-viewer)
[//]: # (   5. Actions syntax: https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#about-yaml-syntax-for-workflows)
[//]: # (   6. Creds management: https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
[//]: # (   7. Context data reference: https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/accessing-contextual-information-about-workflow-runs#context-availability)
[//]: # (   7. Try to split crossbrowser runs using GitHub actions: https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/running-variations-of-jobs-in-a-workflow)
4. Create a github job, to manually trigger the desired suite of tests.
   5. Add ability to set desired browser
   6. Add ability to set desired env
7. Add 1 parametrized test sample https://allurereport.org/docs/pytest-reference/ 
