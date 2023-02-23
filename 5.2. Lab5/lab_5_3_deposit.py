"""
Wyznacz zysk z 3 letniej lokaty bankowej wg. założeń:
• inwestowane środki 46 567,00 zł
• stałe oprocentowanie roczne 7.5%
• coroczna kapitalizacja odsetek
• w obliczeniach zastosuj złożony operator przypisania
"""

investment = 46_567.00
bank_rate = 0.075


# lokata bankowa po roku:
profit1 = investment * bank_rate
deposit1 = investment
deposit1 += profit1


# lokata bankowa po dwóch latach
profit2 = deposit1 * bank_rate
deposit2 = deposit1
deposit2 += profit2


#lokata bankowa po trzech latach
profit3 = deposit2 * bank_rate
deposit3 = deposit2
deposit3 += profit3



print("\n",
"Inwestowane środki:", str(investment), "zł", "\n",
"\n",
"Stałe oprocentowanie roczne wynosi: ", str(bank_rate * 100), "%", "\n",
"\n",
"Po kapitalizacji odsetek:", "\n",
"- po roku zysk wyniesie", str(round(profit1, 2)), "zł",
    "(lokata bankowa będzie wynosić", str(round(deposit1, 2)), "zł)", "\n",
"- po dwóch latach zysk wyniesie w sumie", str(round(profit1 + profit2, 2)), "zł"
    "(lokata bankowa będzie wynosić", str(round(deposit2, 2)), "zł)", "\n",
"- po trzech latach zysk wyniesie w sumie", str(round(profit1 + profit2 + profit3, 2)), "zł",
    "(lokata bankowa będzie wynosić", str(round(deposit3, 2)), "zł)", "\n",
)

