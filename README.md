# LedgerLens — Financial Statement Analyzer

**LedgerLens** is a full-stack web app that extracts key financial KPIs from uploaded PDF financial statements and flags potential red flags such as high leverage, weak margins, or liquidity concerns. It combines a Python-based analysis engine with a React frontend to provide a clean, interactive interface.

---

## Features

- Upload PDF financial statements
- Extract KPIs like Revenue, Net Income, Gross Margin, EBITDA Margin, etc.
- Flag issues using custom financial risk rules (e.g., Debt/Equity > 2)
- Export results to Excel report
- Modern React UI with file upload, dynamic results, and future dashboard capability

---

## Tech Stack

| Layer       | Stack                          |
|-------------|---------------------------------|
| Frontend    | React + Tailwind CSS            |
| Backend     | Flask + Python                  |
| Data        | PyMuPDF, Pandas, OpenPyXL       |
| Hosting     | GitHub Pages (frontend) + Render (backend)

---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ledgerlens.git
cd ledgerlens
```

### 2. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173` (or Vite port) to use the app.

---

## Folder Structure
```
ledgerlens/
├── backend/             # Flask app + KPI logic
│   ├── app.py
│   ├── pdf_parser.py
│   ├── kpi_extractor.py
│   ├── red_flag_rules.py
│   └── report_generator.py
├── frontend/            # React client
│   └── App.jsx
├── outputs/             # Optional Excel outputs
├── requirements.txt     # Python dependencies
├── README.md
```

---

## Example Red Flag Rules
- Debt-to-Equity > 2
- Current Ratio < 1
- EBITDA Margin < 10%
- Revenue YoY decline > 10%

---

## License
MIT License