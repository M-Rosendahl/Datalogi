# shared Directory

The `shared` directory contains code that is reused across multiple data-science projects in this repository.  
Modules in this folder are designed to be general and not tied to a single dataset or problem.

Typical contents:

- `io.py` – common file loading and saving functions (CSV, Excel, JSON, Parquet, etc.)
- `utils.py` – general helper functions (timing, DataFrame preview, simple cleaning helpers)
- `plotting.py` – standard plotting utilities built on matplotlib and seaborn
- `features.py` – generic feature engineering helpers (scaling, encoding, date parts, interactions)

Each project under `projects/` can import these utilities instead of rewriting the same code.

Example usage inside a notebook or script:

```python
from shared.io import load_csv, save_csv
from shared.utils import preview, info
from shared.plotting import set_default_style, plot_hist
from shared.features import scale_numeric, one_hot_encode