realit-singer-python
===================
[![PyPI version](https://badge.fury.io/py/realit-singer-python.svg)](https://badge.fury.io/py/realit-singer-python)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/realit-singer-python.svg)](https://pypi.org/project/realit-singer-python/)
[![License: MIT](https://img.shields.io/badge/License-Apache2-yellow.svg)](https://opensource.org/licenses/Apache-2.0)

Writes the Singer format from Python.

This is a fork of [Singer's singer-python](https://github.com/singer-io/singer-python) made for [PipelineWise](https://transferwise.github.io/pipelinewise) and [Meltano](https://meltano.com/)

Usage
---

### Setup environment
This library depends on python3. We recommend using a `virtualenv` like this:

```bash
python3 -m venv ~/.virtualenvs/singer-python
```

### Installation
Next, install this library:

```bash
source ~/.virtualenvs/singer-python/bin/activate
git clone http://github.com/singer-io/singer-python
cd singer-python
pip install
```

### Usage example
Now, from python code within the same `virtualenv`, you can use the library:

```python
import singer

singer.write_schema('my_table',
	            {'properties':{'id': {'type': 'string', 'key': True}}},
		    ['id'])
singer.write_records('my_table',
                     [{'id': 'b'}, {'id':'d'}])
singer.write_state({'my_table': 'd'})
```

### Logging configuration

**realit-singer-python** by default doesn't use any predefined logging configuration, it's up to the calling 
library to define it. However, if the environment variable `LOGGING_CONF_FILE` is found and set then the **realit-singer-python** 
would use the path provided in the env variable as the logging configuration for the logger. 

### Singer Decimal

Enabling the use_singer_decimal = True in a tap will output **decimal** and **floats** as a string
rather than their numeric representation.

**Optional Setting**:

A boolean setting: when enabled `true` in the config will outputs decimal and floating point numbers as strings to avoid loss of precision and scale.
For supporting taps, there are hints in the schema message, format = "singer.decimal", and additionalProperties scale_precision dictionary providing precision and scale. For decimal data, the target can use this 
information to correctly replicate decimal data without loss. For the Floats and Number data type without precision and scale it is recommended that post processing formats the datatype based on an inspection of the data because the true data size is unknown / dynamic.

```json
{
  "use_singer_decimal": true,
}
```

## Developer Resources

### Initialize your Development Environment

```bash
pip install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests/` directory and
then run:

```bash
poetry run pytest
```

or 

```bash
poetry run coverage run --parallel -m pytest
```

### Continuous Integration
Run through the full suite of tests and linters by running

```bash
poetry run tox
```

These must pass in order for PR's to be merged.


License
-------

Distributed under the Apache License Version 2.0
