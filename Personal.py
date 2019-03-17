"""
Will hold my portfolio and update me on what to do
Run it every Friday Morning/ Weekend
Notes at Bottom
"""
from portfolio import Portfolio
from datetime import date
year = date.today().year
month = date.today().month
day = date.today().day

personal = Portfolio([("Reliance", "BOM500325", "BSE", 1), ("HDFC", "BOM500180", "BSE", 1), ("SBI", "BOM500112", "BSE", 1)])

print(personal.computeActions('bollingerbands'))
personal.display_Graph('bollingerbands')

"""
---------------------------------------------------------------
Starting- 
Stocks to follow - Reliance, HDFC, SBI all on BSE
Starting Capital - 2500 + 2500 + 2500 for each stock up and down
Starting Stock Investment- 3*R (3967 overall), 2*H(4506 overall) 14*s(4168 overall) - OVERALL 12640
Overall Starting Assets - 20,140

---------------------------------------------------------------
"""
