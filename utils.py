# utils.py
# utils.py
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API client with your API key
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")  # Use the valid model name


def evaluate_formula(title, formula):
    prompt = f"""
    The user submitted a formula for "{title}" in machine learning.

    Submitted formula:
    {formula}

    Check if it's correct. Compare with the standard formula.
    Provide feedback and assign a score (1 = correct, 0 = incorrect).
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"

def evaluate_multiple_formulas(formula_list):
    results = []
    for title, formula in formula_list:
        feedback = evaluate_formula(title, formula)
        results.append((title, feedback))
    return results
