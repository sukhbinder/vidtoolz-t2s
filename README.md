# vidtoolz-t2s

[![PyPI](https://img.shields.io/pypi/v/vidtoolz-t2s.svg)](https://pypi.org/project/vidtoolz-t2s/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/vidtoolz-t2s?include_prereleases&label=changelog)](https://github.com/sukhbinder/vidtoolz-t2s/releases)
[![Tests](https://github.com/sukhbinder/vidtoolz-t2s/workflows/Test/badge.svg)](https://github.com/sukhbinder/vidtoolz-t2s/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/vidtoolz-t2s/blob/main/LICENSE)

Text to speech using kokoro for mac os

## Installation

First install [vidtoolz](https://github.com/sukhbinder/vidtoolz).

```bash
pip install vidtoolz
```

Then install this plugin in the same environment as your vidtoolz application.

```bash
vidtoolz install vidtoolz-t2s
```
## Usage

type ``vid t2s --help`` to get help



## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd vidtoolz-t2s
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
