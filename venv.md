# Python Virtual Environment

This repo uses a local virtual environment at `.venv/` (git-ignored).

## Environment

- **Location:** `.venv/` (repo root)
- **Python:** 3.12.3
- **Created with:** `python3 -m venv .venv`

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install --upgrade pip setuptools wheel
.venv/bin/pip install -r requirements.txt
```

## Activate

```bash
source .venv/bin/activate   # bash/zsh
```

Deactivate with `deactivate`. Or run tools directly without activating, e.g. `.venv/bin/python script.py`.

## Dependencies

Third-party packages the Python code imports (see `requirements.txt` for the full pinned list):

| Package | Purpose |
|---|---|
| `numpy` | Array math used throughout the generated models |
| `jax` / `jaxlib` | Autodiff / accelerated evaluation (used by `bsim4_unrolled.py`) |
| `sympy` | Symbolic math |
| `matplotlib` | Plotting of results |
| `setuptools-rust` | Building the Rust-backed `verilogae` module |
| `scipy` | Pulled in as a dependency (jax) |

Local (in-repo) modules — **not** pip packages: `melange`, `verilogae`, `mir_lift_paths` (under `code/OpenVAF-altered/OpenVAF/`).

## Regenerating requirements.txt

```bash
.venv/bin/pip freeze > requirements.txt
```

## Notes

- The Python pipeline (Verilog-A → Python) does not require ngspice — see `PYTHON_PIPELINE.md`.
- Building `openvaf-r` itself uses Rust/Cargo and LLVM, independent of this venv.
