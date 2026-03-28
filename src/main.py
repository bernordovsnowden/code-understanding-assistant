from pathlib import Path

from ingest import load_python_file
from parser import parse_code, extract_structure
from analyzer import analyze_code
from summarizer import summarize_results


def main() -> None:
    input_file = "data/raw_code/sample.py"
    output_dir = Path("data/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)

    code = load_python_file(input_file)
    tree = parse_code(code)
    structure = extract_structure(tree)
    metrics = analyze_code(code, tree)
    summary = summarize_results(structure, metrics)

    output_file = output_dir / "summary.txt"
    output_file.write_text(summary, encoding="utf-8")

    print(summary)
    print(f"\nSaved summary to: {output_file}")


if __name__ == "__main__":
    main()
