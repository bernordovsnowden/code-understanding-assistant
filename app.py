import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Code Understanding Assistant", layout="wide")
st.title("Code Understanding Assistant")
st.write("Upload a Python file and get a quick structural summary.")

api_key = st.secrets.get("OPENAI_API_KEY", None)
client = OpenAI(api_key=api_key) if api_key else None

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

        st.subheader("AI Code Explanation")

        audience = st.selectbox(
            "Explain for:",
            ["Beginner", "Intermediate", "Technical"]
        )

        if st.button("Explain Code in Plain English"):
            if client is None:
                st.error("OpenAI API key is missing. Add OPENAI_API_KEY in Streamlit Secrets.")
        else:
            with st.spinner("Analyzing code with AI..."):
                prompt = f"""
Explain the following Python code in plain English for a {audience.lower()} audience.

Code:
{code}

Provide:
1. What the code does
2. Step-by-step breakdown
3. Key components
4. Any issues or improvements
"""
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

            st.subheader("Explanation")
            st.write(response.output_text)

    except Exception as e:
        st.error(f"App error: {e}")