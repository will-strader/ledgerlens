from flask import Flask, request, jsonify
from flask_cors import CORS
import tempfile
from pdf_parser import extract_text_from_pdf, extract_financial_sections
from kpi_extractor import extract_kpis
from red_flag_rules import detect_red_flags

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files["file"]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        file.save(tmp.name)
        text = extract_text_from_pdf(tmp.name)
        lines = extract_financial_sections(text)
        kpis = extract_kpis(lines)
        flags = detect_red_flags(kpis)
    return jsonify({ "kpis": kpis, "flags": flags })

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)