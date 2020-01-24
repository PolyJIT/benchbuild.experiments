# benchbuild.experiments

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This includes a set of experiments curated by benchbuild that serves as reference implementation for experiments in benchbuild.

## Experiments:

- raw: An experiment that runs all projects wrapped in the time command storing the result. This showcases a simple timing measurement,
       without any further customization or precautions for the experiment itself.
- empty: An experiment that does nothing. This just compiles and runs all projects.

## Installation

benchbuild.experiments is available via PyPI. You can install the latest release with pip.
```bash
# Global install
$ pip install benchbuild.experiments
# Local install
$ pip install --user benchbuild.experiments
```

```bash
# Recommended: Install into a virutalenv.
$ virtualenv benchbuild
...
$ source benchbuild/bin/activate
...
$ pip install benchbuild
```

Make sure you specify the experiments you want to load in benchbuild's configuration. The environment variable is named:
``BB_PLUGINS_EXPERIMENTS``. Please refer to benchbuild's configuration dump for details.
