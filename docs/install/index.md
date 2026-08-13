# Installation guide

You can install netZooPy through pip or through conda. Below, you will find
all the steps and requirements for both cases.

## PIP installation

### Requirements

netZooPy requires Python 3. `pip` installs the following dependencies
automatically, so you normally do not need to install them by hand:

- h5py
- pandas
- numpy
- networkx
- matplotlib
- scipy
- python-igraph
- joblib
- statsmodels
- scikit-learn
- click
- tables (PyTables)
- torch (PyTorch)

GPU acceleration (the `gpu` computing option in PANDA, LIONESS, PUMA and OTTER)
additionally requires [CuPy](https://cupy.dev). CuPy is **not** installed
automatically because the right build depends on your CUDA version — install
the one that matches your toolkit, e.g. `pip install cupy-cuda12x`.

### Install

We recommend installing netZooPy inside a dedicated virtual environment so it
stays isolated from your other projects:

```bash
python3 -m venv netzoo-env
source netzoo-env/bin/activate          # Windows: netzoo-env\Scripts\activate
git clone https://github.com/netZoo/netZooPy.git
cd netZooPy
pip3 install -e .
```

Then you can import netZooPy and its modules in your code:

```python
import netZooPy
from netZooPy.cobra import cobra
```

### Troubleshooting

**`import netZooPy` works but a submodule import fails** — for example
`from netZooPy.cobra import cobra` raises
`ModuleNotFoundError: No module named 'netZooPy.cobra'`, or you see
`ImportError: cannot import name 'cobra' from 'netZooPy' (unknown location)`.

This means Python is importing the cloned *source folder* instead of the
installed package. It usually happens when:

- you start Python (or a Jupyter / VS Code notebook kernel) from the directory
  that *contains* the cloned `netZooPy` folder — the folder name then shadows
  the installed package as an empty namespace package; or
- the active interpreter / kernel is not the same environment where you ran
  `pip3 install -e .` (a common mismatch in VS Code and Jupyter).

Quick check: run `python -c "import netZooPy; print(netZooPy.__file__)"`. If it
prints `None`, you are loading the empty namespace folder rather than the
package. To fix it, make sure your interpreter / notebook kernel is the
environment where netZooPy is installed, and start Python from a directory
other than the one containing the clone.

**`ModuleNotFoundError: No module named 'sklearn'`** when importing COBRA means
scikit-learn is missing. Update to the latest netZooPy (scikit-learn is now a
declared dependency) or install it manually with `pip install scikit-learn`.

For any other installation issue or function bug, please open an
[issue](https://github.com/netZoo/netZooPy/issues) on GitHub.


## Conda installation

On anaconda.org you will find the conda recipes for all platforms. We recommend using conda environments to keep your analyses self-contained and reproducible.

To install netzoopy through conda:

```bash
conda install -c netzoo -c conda-forge netzoopy
```
