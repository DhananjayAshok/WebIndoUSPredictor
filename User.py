from stock import Stock
from portfolio import Portfolio
from typing import List, Dict, Tuple
import datetime

#a = Stock("HDFC","BOM500180", "INTERNAL", ((2017, 4, 2) ,(2019, 2, 20)))
#print((a.df))
#info = a.implimentAnalysis("bollingerbands")
#a.create_Graph('bollingerbands', info)
#print(a.strategy)
#r = a.simulateAnalysis("bollingerbands", (2018, 4, 25))
#print(r)
p = Portfolio([("HDFC","BOM500180", "BSE"), ("Apple Industries", "AAPL", "NASDAQ")], ((2017, 2, 2) ,(2019, 2, 20)))
print(p.simulateAnalysis("bollingerbands", (2017, 4, 22)))
