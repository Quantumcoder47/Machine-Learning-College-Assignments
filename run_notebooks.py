"""
run_notebooks.py

Lightweight smoke-test runner for all `model.ipynb` notebooks in the repo.
It attempts to execute each notebook (in-place) and reports success/failure.

Usage:
  python run_notebooks.py

Notes:
- Uses nbformat + nbconvert ExecutePreprocessor. Install with `pip install nbformat nbconvert`.
- Long-running notebooks may time out; increase TIMEOUT_SECONDS as needed.
"""
import glob
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

ROOT = os.path.dirname(__file__)
NOTEBOOK_PATTERN = os.path.join(ROOT, "**", "model.ipynb")
TIMEOUT_SECONDS = 600  # per-notebook timeout (increase for heavy notebooks)


def run_notebook(path: str, timeout: int = TIMEOUT_SECONDS) -> (bool, str):
    """Execute a notebook and return (success, message)."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        ep = ExecutePreprocessor(timeout=timeout, kernel_name="python3")
        ep.preprocess(nb, {"metadata": {"path": os.path.dirname(path)}})

        # Optionally overwrite notebook with outputs (in-place)
        with open(path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)

        return True, "OK"
    except Exception as e:
        return False, str(e)


def main():
    notebooks = sorted(glob.glob(NOTEBOOK_PATTERN, recursive=True))
    if not notebooks:
        print("No notebooks found (pattern: {}")
        return

    print(f"Found {len(notebooks)} notebook(s). Running smoke tests (timeout={TIMEOUT_SECONDS}s each)\n")
    summary = []

    for nb in notebooks:
        rel = os.path.relpath(nb, ROOT)
        print(f"-> Executing: {rel}")
        success, msg = run_notebook(nb)
        if success:
            print(f"   ✔ Success: {rel}\n")
        else:
            print(f"   ✖ Failed: {rel}\n     Error: {msg}\n")
        summary.append((rel, success, msg))

    # Print summary
    print("\n=== SUMMARY ===")
    ok = [s for s in summary if s[1]]
    failed = [s for s in summary if not s[1]]
    print(f"Total: {len(summary)}, Passed: {len(ok)}, Failed: {len(failed)}")
    if failed:
        print("\nFailed notebooks:")
        for rel, _, msg in failed:
            print(f" - {rel}: {msg.splitlines()[0]}")
        raise SystemExit(2)
    else:
        print("\nAll notebooks executed successfully.")


if __name__ == "__main__":
    main()
