import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.parser import parse_code, extract_structure


def test_parse_and_extract_structure():
    code = """
import os

class MyClass:
    pass

def hello():
    return "hi"
"""
    tree = parse_code(code)
    structure = extract_structure(tree)

    assert "hello" in structure["functions"]
    assert "MyClass" in structure["classes"]
    assert "os" in structure["imports"]