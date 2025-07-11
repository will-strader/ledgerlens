from pdf_parser import extract_text_from_pdf, extract_financial_sections
from kpi_extractor import extract_kpis
from red_flag_rules import detect_red_flags

def run_pipeline(pdf_path):
    print(f"Processing: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)
    lines = extract_financial_sections(text)
    kpis = extract_kpis(lines)
    flags = detect_red_flags(kpis)

    print("Extracted KPIs:")
    for k, v in kpis.items():
        print(f"  {k}: {v}")
    
    print("\nRed Flags:")
    for f in flags:
        print(f"  ⚠️ {f}")

if __name__ == "__main__":
    test_pdf = "data/sample1.pdf"
    run_pipeline(test_pdf)