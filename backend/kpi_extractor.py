import re

def parse_numeric(value):
    try:
        return float(value.replace(',', '').replace('$', '').strip())
    except:
        return None

def extract_kpis(lines):
    kpis = {}
    for line in lines:
        if "Revenue" in line and "Net" not in line:
            kpis['Revenue'] = parse_numeric(line)
        elif "Net Income" in line:
            kpis['Net Income'] = parse_numeric(line)
        elif "Operating Expenses" in line:
            kpis['Operating Expenses'] = parse_numeric(line)
        elif "EBITDA" in line:
            kpis['EBITDA'] = parse_numeric(line)
        elif "Current Assets" in line:
            kpis['Current Assets'] = parse_numeric(line)
        elif "Current Liabilities" in line:
            kpis['Current Liabilities'] = parse_numeric(line)
        elif "Total Debt" in line:
            kpis['Total Debt'] = parse_numeric(line)
        elif "Shareholders’ Equity" in line or "Shareholder Equity" in line:
            kpis['Shareholders’ Equity'] = parse_numeric(line)
        elif "Interest Expense" in line:
            kpis['Interest Expense'] = parse_numeric(line)

    # KPI Calculations (add more calculations as needed)
    if 'Revenue' in kpis and 'Operating Expenses' in kpis:
        kpis['Gross Margin'] = kpis['Revenue'] - kpis['Operating Expenses']
    if 'Revenue' in kpis and 'EBITDA' in kpis:
        kpis['EBITDA Margin'] = kpis['EBITDA'] / kpis['Revenue'] if kpis['Revenue'] else None
    if 'Revenue' in kpis and 'Net Income' in kpis:
        kpis['Net Income Margin'] = kpis['Net Income'] / kpis['Revenue'] if kpis['Revenue'] else None
    if 'Current Assets' in kpis and 'Current Liabilities' in kpis:
        kpis['Current Ratio'] = kpis['Current Assets'] / kpis['Current Liabilities'] if kpis['Current Liabilities'] else None
    if 'Total Debt' in kpis and 'Shareholders’ Equity' in kpis:
        kpis['Debt to Equity'] = kpis['Total Debt'] / kpis['Shareholders’ Equity'] if kpis['Shareholders’ Equity'] else None
    if 'EBITDA' in kpis and 'Interest Expense' in kpis:
        kpis['Interest Coverage Ratio'] = kpis['EBITDA'] / kpis['Interest Expense'] if kpis['Interest Expense'] else None

    return kpis