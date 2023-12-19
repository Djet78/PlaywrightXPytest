[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[//]: # ([![pre-commit]&#40;https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&#41;]&#40;https://github.com/pre-commit/pre-commit&#41;)

# Playwright X Pytest X <report_tool>
Playwright in combination with Pytest test framework, and <report_tool> retorting example.

#### Used python main packages:
1. `playwright` - Test runner
4. `requrests` - API interactions 
5. `poetry` - Dependencies management
6. `ruff` - Linter and formatting tool

---

## Setup for Windows

[//]: # (### 1. Install Allure )

[//]: # (1. Download Java 21 : https://www.oracle.com/java/technologies/downloads/)

[//]: # (2. Set `JAVA_HOME` environment variable, point it to the java root folder.)

[//]: # (3. Download and unpack latest allure release: https://github.com/allure-framework/allure2/releases)

[//]: # (   1. Or using Scoop: https://allurereport.org/docs/gettingstarted-installation/#install-via-scoop-for-windows)

[//]: # (4. Into `PATH` - add path to the allure.bat file. Ex: `*\allure\allure-2.24.1\bin`)


### 2. Install Poetry
1. Install pipx via pip - https://github.com/pypa/pipx?tab=readme-ov-file
2. Install poetry via pipx - https://python-poetry.org/docs/#installing-with-pipx 
3. Add poetry executable into `PATH`. Ex: `c:\users\test\.local\bin`



### 3. Configure local project: 
1. Clone the repo
2. Run `git submodules update --init --recursive`
3. In the project root dir - run `poetry install`
4. Activate created env: `.\.venv\Scripts\activate`
5. Apply pre-commit hooks: `pre-commit install`
6. Install webdrivers `playwright install`


---



## TODO
 
1. Add some sample tests using Playwright
2. Find reporting tools for playwright
   2. Allure (using allure-pytest) - https://github.com/microsoft/playwright-python/issues/1265
   3. Lambdatest (Seems have a freemium plan)- https://www.lambdatest.com/support/docs/pytest-on-hyperexecute/
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
3. Configure CI/CD for app, using GitHub actions 
4. 