import ast
from typing import Any, Dict, List


def parse_code(code: str) -> ast.AST:
    """
    Parse Python source code into an AST.
    """
    try:
        return ast.parse(code)
    except SyntaxError as exc:
        raise SyntaxError(f"Invalid Python code: {exc}") from exc


def extract_structure(tree: ast.AST) -> Dict[str, List[str]]:
    """
    Extract top-level functions, classes, and imports from the AST.
    """
    functions: List[str] = []
    classes: List[str] = []
    imports: List[str] = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            module = node.module if node.module else ""
            for alias in node.names:
                imports.append(f"{module}.{alias.name}" if module else alias.name)

    return {
        "functions": sorted(set(functions)),
        "classes": sorted(set(classes)),
        "imports": sorted(set(imports)),
    }
