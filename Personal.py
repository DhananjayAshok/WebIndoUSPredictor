"""
Will hold my portfolio and update me on what to do
Run it every Friday Morning
Capital starting: 
10,000
"""
from portfolio import Portfolio
from datetime import date
year = date.today().year
month = date.today().month
day = date.today().day

personal = Portfolio([("Reliance", "BOM500325", "BSE"), ("HDFC", "BOM500180", "BSE"), ("SBI", "BOM500112", "BSE")])

print(personal.computeActions('bollingerbands'))
personal.display_Graph('bollingerbands')