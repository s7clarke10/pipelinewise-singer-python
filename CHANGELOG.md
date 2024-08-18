# Changelog

## 5.0.3 (2024-08-19)
 * Moving to a trusted push to pypi

## 5.0.2 (2024-08-13)
 * Bump black from 24.4.2 to 24.8.0
 * Bump pylint from 3.2.5 to 3.2.6
 * Bump mypy from 1.10.1 to 1.11.1
 * Bump flake8 from 7.1.0 to 7.1.1 
 * Bump actions/setup-python from 3 to 5
 * Bump pypa/gh-action-pypi-publish from 1.4.2 to 1.9.0

## 5.0.1 (2024-08-12)
 * Updating the README.md to have the badges point to the correctly published version on PyPI.

## 5.0.0 (2024-08-09)
 * Renaming repo to realit-singer-python to allow required publishing to PyPI
 * NOTE: Will need to urgently update tap-oracle, tap-mssql, tap-s3-csv which are dependent on this.

## 4.0.1 (2024-08-08)
 * Correcting Supported Python version constraint in pyproject.toml >=3.8,<3.13
 * Bump pytest from 7.4.4 to 8.3.2
 * Bump pytz from 2018.9 to 2024.1
 * Bump jsonschema from 4.22.0 to 4.23.0
 * Bump tox from 4.15.1 to 4.17.1 #35
 * Bump coverage from 7.5.4 to 7.6.1 #33

## 4.0.0 (2024-07-08)
 * Moving from setup.py to pyproject.toml and poetry for installation
 * Introducing tox for platform independent testing of pep8 compliance.
 * Introducing black for formatting
 * Introducing isort for compliant and order includes
 * Introducing flake8 for linting alongside pylint
 * Introducing mypy for type checking
 * Updating github actions to run tox tests rather than directly running pytests.
 * Code formatting updates and changes to pass / met the standards above.

## 3.0.0 (2023-08-23)
 * Using msgspec instead of orjson or other serializers for speed benefit
 * Support for Python 3.12
 * Deprecating Python 3.7

## 2.0.2 (2022-03-23)
 * Using orjson instead of simplejson or other serializers for speed benefit
 * Fix: Output decimal.Decimal as int or float not str

## 2.0.1 (2021-11-23)
  * Fixed an issue when `format_message` returned newline character

## 2.0.0 (2021-11-23)
  * Swith to `orjson` JSON library to serialie and deserialise faster
  * Bump `backoff` to 1.11.1
  * Bump `pytz` to latest

## 1.3.0 (2021-08-12)
  * Added `time_extracted` to BATCH message type

## 1.2.0 (2020-12-01)
  * Add BATCH message type

## 1.1.4 (2020-11-05)
  * Update pytz pin to wider range

## 1.1.3 (2020-06-11)
  * Bump jsonschema to 3.2.0

## 1.1.2 (2020-04-29)
  * Bump pytz to 2020.1

## 1.1.1 (2020-03-19)
  * Bump pytz to 2019.3

## 1.1.0 (2020-02-17)
  * Added a logging config file to fallback to in case LOGGING_CONF_FILE env variable is not defined. This is to 
  respect the singer specs that requires the logs to be sent to stderr and not stdout.

## 1.0.0 (2020-02-06)
  * Initial version (fork of https://github.com/singer-io/singer-python version 5.9.0)
