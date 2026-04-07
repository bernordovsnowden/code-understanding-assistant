import streamlit as st

st.set_page_config(page_title="Code Understanding Assistant", layout="wide")
st.title("Code Understanding Assistant")
st.write("Upload a Python file and get a quick structural summary.")

try:
    from src.parser import parse_code, extract_structure
    from src.analyzer import analyze_code
    from src.summarizer import summarize_results
except Exception as e:
    st.error(f"Import error: {e}")
    st.stop()

uploaded_file = st.file_uploader("Upload a .py file", type=["py"])

if uploaded_file is not None:
    try:
        code = uploaded_file.read().decode("utf-8")

        st.subheader("Code Preview")
        st.code(code, language="python")

        tree = parse_code(code)
        structure = extract_structure(tree)
        metrics = analyze_code(code, tree)
        summary = summarize_results(structure, metrics)

        st.subheader("Summary")
        st.text(summary)

        st.subheader("Extracted Structure")
        st.write(structure)

        st.subheader("Metrics")
        st.write(metrics)

    except Exception as e:
        st.error(f"App error: {e}")