def date_greater_than_or_equal_to(d1, d2) -> bool:
    """
    d1, d2 are datetime objects
    Returns True iff d1 >= d2
    """
    return (d1 - d2).days >= 0

def date_within_range(sample_date, start_date, end_date)->bool:
    """
    Returns True iff sample_date is within the range of the two provided dates, not inclusive
    all variables are datetime objects
    """
    if date_greater_than_or_equal_to(start_date, sample_date):
        return False
    if date_greater_than_or_equal_to(sample_date, end_date):
        return False
    return True

def date_within_days(d1, d2, day_gap)->bool:
    """
    Returns True iff the two dates are within "day_gap" days of each other
    """
    if date_greater_than_or_equal_to(d1, d2):
        return ((d1-d2).days - day_gap) >= 0
    else:
        return ((d2-d1).days - day_gap) >= 0
    

class OutDatedError(Exception):
    def __str__(self):
        return "Attempting to call a date that is not within the stock data"


class InsufficientDataError(Exception):
    def __str__(self):
        return "Amount of data given is insufficient to predict action"