def detect_red_flags(kpis):
    flags = []

    # Liquidity risk
    if kpis.get('Current Ratio', 1) < 1:
        flags.append("Current ratio below 1 — liquidity risk")

    # Profitability concerns
    if kpis.get('Gross Margin', 999) < 0.2:
        flags.append("Low gross margin — potential pricing/cost issue")
    if kpis.get('EBITDA Margin', 999) < 0.1:
        flags.append("EBITDA margin under 10% — weak operating performance")
    if kpis.get('Net Income Margin', 999) < 0.05:
        flags.append("Low net income margin — profitability concern")

    # Leverage risk
    if kpis.get('Debt to Equity', 0) > 2:
        flags.append("High debt-to-equity ratio — leverage risk")
    if kpis.get('Interest Coverage Ratio', 999) < 1.5:
        flags.append("Low interest coverage — risk of debt servicing problems")

    # Growth indicators (requires YoY data if we have it)
    if kpis.get('Revenue Growth YoY', 0) < -0.1:
        flags.append("Revenue declined more than 10% YoY")
    if kpis.get('EBITDA Growth YoY', 0) < -0.1:
        flags.append("EBITDA decline — operational deterioration")

    return flags