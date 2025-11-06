# Optimization problems in Steelmaking

A small repository collecting models, examples and utilities for formulating and
solving optimization problems found in steelmaking using python.


## Getting started

Requirements
- Python 3.10+
- Recommended packages: numpy, pandas, scipy, matplotlib, pyomo, jupyter

Create a virtual environment and install the recommended packages:

```bash
python3 -m venv .venv
source .venv/bin/activate   # or: . .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Ensure that the following solvers are installed and configured to be used with Pyomo:
- HiGHS
- SCIP

## Project structure

- `models/` — optimization models (Python files, Pyomo models)
- `data/` — example CSVs and datasets
- `notebooks/` — Jupyter notebooks with worked examples
- `utils/` — helpers for data loading, plotting, post-processing

## Contributing

Contributions are welcome. Please open an issue to discuss larger changes,
or submit a pull request with a clear description of the model/example and a
small dataset or notebook showing how to run it.

## License

This project is provided under the terms of the LICENSE in this repository.


