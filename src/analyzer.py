import ast
from typing import Dict


def analyze_code(code: str, tree: ast.AST) -> Dict[str, int]:
    """
    Compute simple code metrics.
    """
    lines = [line for line in code.splitlines() if line.strip()]
    function_count = sum(isinstance(node, ast.FunctionDef) for node in ast.walk(tree))
    class_count = sum(isinstance(node, ast.ClassDef) for node in ast.walk(tree))
    import_count = sum(
        isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(tree)
    )

    return {
        "non_empty_lines": len(lines),
        "function_count": function_count,
        "class_count": class_count,
        "import_count": import_count,
    }
