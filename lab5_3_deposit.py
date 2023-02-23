"""
Wyznacz zysk z 3 letniej lokaty bankowej wg założeń:
• inwestowane środki 46 567,00 zł
• stałe oprocentowanie roczne 7.5%
• coroczna kapitalizacja odsetek
• w obliczeniach zastosuj złożony operator przypisania
"""

inwestment = 46_567
deposit = inwestment
year_factor = 1.075

inwestment *= year_factor
inwestment *= year_factor
inwestment *= year_factor

print("Zysk inwestycji wynosi ", round(deposit - inwestment, 2), "zł.")