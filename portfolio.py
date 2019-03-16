from typing import Tuple, List, Dict, Any, Union, Optional
from stock import Stock
import utility
import datetime




class Portfolio(object):
    """A collection of Stocks"""
    def __init__(self, stocks: List[Tuple[str, str, str]]):
        """
        Create a new Portfolio object
        stocks to be in format: (name, ticker, exchange)
        """
        self.stocks = stocks
        self.stocks = []
        for stock in stocks:
            a = Stock(stock[0], stock[1],stock[2])
            self.stocks.append(a)
        return

    def computeActions(self,method) -> Dict:
        """
        Returns a dictionary: The output is a dictionary of format: {ticker: Strategy}

        """
        final = {}
        for stock in self.stocks:
            stock.implimentAnalysis(method)
            final[str(stock) + " on " + utility.represent_date(stock.end_date)] = stock.strategy
        return final
    
    def simulateAnalysis(self, method: str, start_date, frequency = 7)  -> Dict:
        """
        Returns a dictionary: THe output is a dictionary of format : {ticker: % Gain or Loss}
        start_date: is in format (YYYY, MM, DD) with YYYY, MM and DD as integers
        frequency: integer that represents the number of days between each trade
        --------------------------------------------------------------------------------------
        Current Options
        --------------------------------------------------------------------------------------
        1. Bollinger Band Analysis : 'bollingerbands'
        """
        final = {}
        for stock in self.stocks:
            final[str(stock)] = stock.simulateAnalysis(method, start_date, frequency)

        return final

    def display_Graph(self, method: str):
        for stock in self.stocks:
            info = stock.implimentAnalysis(method)
            stock.create_Graph(method,info)

