from stock import Stock
from portfolio import Portfolio
from typing import List, Dict, Tuple
import datetime

a = Stock("Reliance","BOM500325", "BSE")
#print(a.df)
#print(a.get_current_price())
#print(type(a.get_current_price()))
print(a.simulateAnalysis('bollingerbands', (2018, 8, 1)))
#info = a.implimentAnalysis("bollingerbands")
#print(a.strategy)
#a.create_Graph("bollingerbands", info)

#sherman = Portfolio([("Electronic Arts", "EA", "NASDAQ", 1), ("Baidu","BIDU","NASDAQ", 1), ("Adobe","ADBE","NASDAQ", 1), ("Amazon", "AMZN", "NASDAQ", 1), ("Bill Gates Penis", "MSFT", "NASDAQ", 1)], capital = 1000)
#sherman.buy_stock(("HDFC", "BOM500180", "BSE", 1))
#print(sherman.capital)
#sherman.sell_stock("Electronic Arts", 2)
#print(sherman.get_init_data())
#print(sherman.computeActions("bollingerbands"))
#print(sherman.simulateAnalysis('bollingerbands', (2018, 3, 16)))
#sherman.display_Graph("bollingerbands")
