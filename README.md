# FAOSTAT data

<!---
Can use start-after and end-before directives in docs, see
https://myst-parser.readthedocs.io/en/latest/syntax/organising_content.html#inserting-other-documents-directly-into-the-current-document
-->

<!--- sec-begin-description -->

Download and process FAOSTAT data



[![CI](https://github.com/primap-community/FAOSTAT_data_primap/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/primap-community/FAOSTAT_data_primap/actions/workflows/ci.yaml)
[![Coverage](https://codecov.io/gh/primap-community/FAOSTAT_data_primap/branch/main/graph/badge.svg)](https://codecov.io/gh/primap-community/FAOSTAT_data_primap)
[![Docs](https://readthedocs.org/projects/faostat-data-primap/badge/?version=latest)](https://faostat-data-primap.readthedocs.io)

**PyPI :**
[![PyPI](https://img.shields.io/pypi/v/faostat-data-primap.svg)](https://pypi.org/project/faostat-data-primap/)
[![PyPI: Supported Python versions](https://img.shields.io/pypi/pyversions/faostat-data-primap.svg)](https://pypi.org/project/faostat-data-primap/)
[![PyPI install](https://github.com/primap-community/FAOSTAT_data_primap/actions/workflows/install.yaml/badge.svg?branch=main)](https://github.com/primap-community/FAOSTAT_data_primap/actions/workflows/install.yaml)

**Other info :**
[![Licence](https://img.shields.io/github/license/primap-community/FAOSTAT_data_primap.svg)](https://github.com/primap-community/FAOSTAT_data_primap/blob/main/LICENCE)
[![Last Commit](https://img.shields.io/github/last-commit/primap-community/FAOSTAT_data_primap.svg)](https://github.com/primap-community/FAOSTAT_data_primap/commits/main)
[![Contributors](https://img.shields.io/github/contributors/primap-community/FAOSTAT_data_primap.svg)](https://github.com/primap-community/FAOSTAT_data_primap/graphs/contributors)


<!--- sec-end-description -->

Full documentation can be found at:
[faostat-data-primap.readthedocs.io](https://faostat-data-primap.readthedocs.io/en/latest/).
We recommend reading the docs there because the internal documentation links
don't render correctly on GitHub's viewer.

## Installation

<!--- sec-begin-installation -->

FAOSTAT data can be installed with pip, mamba or conda:

```bash
pip install faostat-data-primap
mamba install -c conda-forge faostat-data-primap
conda install -c conda-forge faostat-data-primap
```


<!--- sec-end-installation -->

### For developers

<!--- sec-begin-installation-dev -->

For development, we rely on [poetry](https://python-poetry.org) for all our
dependency management. To get started, you will need to make sure that poetry
is installed
([instructions here](https://python-poetry.org/docs/#installing-with-the-official-installer),
we found that pipx and pip worked better to install on a Mac).

For all of work, we use our `Makefile`.
You can read the instructions out and run the commands by hand if you wish,
but we generally discourage this because it can be error prone.
In order to create your environment, run `make virtual-environment`.

If there are any issues, the messages from the `Makefile` should guide you
through. If not, please raise an issue in the
[issue tracker](https://github.com/primap-community/FAOSTAT_data_primap/issues).

For the rest of our developer docs, please see [](development-reference).

<!--- sec-end-installation-dev -->
