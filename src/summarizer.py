from typing import Dict, List


def summarize_results(structure: Dict[str, List[str]], metrics: Dict[str, int]) -> str:
    """
    Convert extracted structure and metrics into a readable summary.
    """
    functions = ", ".join(structure["functions"]) if structure["functions"] else "None"
    classes = ", ".join(structure["classes"]) if structure["classes"] else "None"
    imports = ", ".join(structure["imports"]) if structure["imports"] else "None"

    summary = f"""
Code Summary
------------
Non-empty lines: {metrics['non_empty_lines']}
Functions: {metrics['function_count']}
Classes: {metrics['class_count']}
Imports: {metrics['import_count']}

Function names: {functions}
Class names: {classes}
Imports used: {imports}
""".strip()

    return summary
