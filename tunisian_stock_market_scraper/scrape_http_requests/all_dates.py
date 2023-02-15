from datetime import date
from dateutil.relativedelta import relativedelta

def get_all_dates():
    calendar=[]
    start=date(2010,1,1)
    next_date = start + relativedelta(days=+89)
    while next_date<date(2023,1,1):
        calendar.append([str(start),str(next_date)])
        start=next_date
        next_date = next_date + relativedelta(days=+89)
    next_date=date(2022,12,31)
    calendar.append([str(start),str(next_date)])
    return calendar
