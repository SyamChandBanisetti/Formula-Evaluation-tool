# app.py
import streamlit as st
from utils import evaluate_multiple_formulas

st.set_page_config(page_title="ML Formula Evaluator", layout="centered")
st.title("📐 ML Formula Evaluator")

st.markdown("Evaluate multiple ML formulas at once. 1 point for each correct formula.")

# Number of formulas user wants to submit
num_formulas = st.number_input("➕ How many formulas do you want to submit?", min_value=1, max_value=10, value=1)

user_inputs = []

for i in range(num_formulas):
    st.markdown(f"### Formula {i + 1}")
    title = st.text_input(f"🧩 Title {i + 1}", key=f"title_{i}")
    formula = st.text_area(f"✍️ Formula {i + 1}", key=f"formula_{i}", height=100)
    user_inputs.append((title, formula))

if st.button("✅ Evaluate All"):
    incomplete = any(not title or not formula.strip() for title, formula in user_inputs)
    if incomplete:
        st.warning("Please fill in all title and formula fields.")
    else:
        with st.spinner("Evaluating all formulas..."):
            results = evaluate_multiple_formulas(user_inputs)

        for idx, (title, feedback) in enumerate(results):
            st.subheader(f"📝 Result for Formula {idx + 1} ({title})")
            st.markdown(feedback)
