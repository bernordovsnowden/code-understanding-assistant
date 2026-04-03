from pathlib import Path


def load_python_file(file_path: str) -> str:
    """
    Load a Python file and return its contents as text.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix != ".py":
        raise ValueError(f"Expected a .py file, got: {path.suffix}")

    return path.read_text(encoding="utf-8")
