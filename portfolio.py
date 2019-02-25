from typing import Tuple, List, Dict, Any, Union, Optional
from stock import Stock
import utility
import datetime




class Portfolio(object):
    """A collection of Stocks"""
    def __init__(self, stocks: List[Tuple], dates: Tuple):
        """
        Create a new Portfolio object
        stocks to be in format: (name, ticker, exchange)
        dates: is in format ( (YYYY, MM, DD), (YYYY, MM, DD) ) with YYYY, MM and DD as integers
            dates will be saved as a datetime object
        """
        self.stocks = stocks
        self.stocks = []
        for stock in stocks:
            a = Stock(stock[0], stock[1],stock[2], dates)
            self.stocks.append(a)
        o = datetime.datetime(dates[0][0], dates[0][1], dates[0][2])
        n = datetime.datetime(dates[1][0], dates[1][1], dates[1][2])
        self.dates = (o, n)
        return

    def computeActions(self,method, date) -> Dict:
        """
        date: is in format (YYYY, MM, DD) with YYYY, MM and DD as integers
        Returns a dictionary: The output is a dictionary of format: {ticker: Strategy}

        """
        date = datetime.datetime(date[0], date[1], date[2])
        final = {}
        today = datetime.date.today()
        if not utility.date_within_range(date, self.dates[0], self.dates[1]):
            raise utility.OutDatedError
        for stock in self.stocks:
            stock.implimentAnalysis(method)
            final[str(stock)] = stock.strategy
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

