import numpy as np

def calculate_portfolio_values(m_n, sigma_n, m_q, x_n, sigma_pn):
    m_pn = (x_n * m_n + (1 - x_n) * m_q) / 100

    sigma_pn_calculated = np.sqrt((x_n**2 * sigma_n**2 + (1 - x_n)**2 * sigma_pn**2)) / 100
    
    return m_pn, sigma_pn_calculated

table_data = [
    {'m_n': 50, 'sigma_n': 20, 'm_q': 10, 'x_n': 80, 'sigma_pn': 15},
    {'m_n': 40, 'sigma_n': 15, 'm_q': 10, 'x_n': 60, 'sigma_pn': 11},
    {'m_n': 50, 'sigma_n': 20, 'm_q': 10, 'x_n': 120, 'sigma_pn': 15},
    {'m_n': 50, 'sigma_n': 20, 'm_q': 10, 'x_n': 75, 'sigma_pn': 12},
    {'m_n': 40, 'sigma_n': 15, 'm_q': 10, 'x_n': 70, 'sigma_pn': 10},
    {'m_n': 30, 'sigma_n': 12, 'm_q': 10, 'x_n': 110, 'sigma_pn': 5},
    {'m_n': 40, 'sigma_n': 15, 'm_q': 10, 'x_n': 90, 'sigma_pn': 12},
    {'m_n': 30, 'sigma_n': 14, 'm_q': 10, 'x_n': 70, 'sigma_pn': 8},
    {'m_n': 50, 'sigma_n': 20, 'm_q': 10, 'x_n': 85, 'sigma_pn': 10},
    {'m_n': 30, 'sigma_n': 13, 'm_q': 10, 'x_n': 55, 'sigma_pn': 11},
]

results = []

for row in table_data:
    m_pn, sigma_pn_calculated = calculate_portfolio_values(
        row['m_n'], row['sigma_n'], row['m_q'], row['x_n'], row['sigma_pn']
    )
    results.append({
        'm_n': row['m_n'],
        'sigma_n': row['sigma_n'],
        'x_n': row['x_n'],
        'm_pn': m_pn,
        'sigma_pn_calculated': sigma_pn_calculated
    })

for res in results:
    print(f"Для m_n = {res['m_n']}%, sigma_n = {res['sigma_n']}%, x_n = {res['x_n']}%:")
    print(f" - Очікувана норма прибутку портфеля: {res['m_pn']:.2f}%")
    print(f" - Оцінка ризику портфеля: {res['sigma_pn_calculated']:.2f}%\n")
