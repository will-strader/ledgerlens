import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def extract_financial_sections(text):
    # Simplistic example for demo purposes
    lines = text.split('\n')
    relevant_lines = [line for line in lines if re.search(r'\$[\d,]+', line)]
    return relevant_lines
