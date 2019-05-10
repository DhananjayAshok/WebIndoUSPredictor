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
Using the following scheme
    If program says sell x% I sell that x%
    If program says buy with x% of capital I do Total Capital/3 * x% and buy with that amount
Stocks to follow - Reliance, HDFC, SBI all on BSE
Starting Capital - 2500 + 2500 + 2500 for each stock up and down
Starting Stock Investment- 3*R (3967 overall), 2*H(4506 overall) 14*s(4168 overall) - OVERALL 12640
Overall Starting Assets - 20,140

---------------------------------------------------------------
23-03-2019
Sell HDFC All (2 shares)
Capital - 7500 + 2*2276 = 12,052
----------------------------------------------------------------
30-03-2019
Sell SBI 100% (14 shares)
Capital - 12,052+ 14*(320.80) = 16,543.2
----------------------------------------------------------------
05-04-2019
No Action
----------------------------------------------------------------
12-04-2019
Buy HDFC (2 Shares) -  
Capital - 16,543.2 - 2*(2,257) = 12,029.2
----------------------------------------------------------------
19-04-2019
Sell HDFC (1 Shares)-
Capital - 12,029.2 + 1*(2,290) = 14,319.2
"""
