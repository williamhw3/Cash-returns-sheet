import datetime
import pandas as pd
from datetime import date, timedelta

today = date.today() - timedelta(days=1)
today = today.strftime("%m/%d/%Y")
start = datetime.datetime.strptime("01/01/1950", "%m/%d/%Y")
end = datetime.datetime.strptime(today, "%m/%d/%Y")
date_generated = pd.date_range(start, end)
print (date_generated.strftime("%m/%d/%Y"))
print(date_generated)
dates = []
for i,c in enumerate(date_generated.strftime("%m/%d/%Y")):
    dates.append([c,1])
df = pd.DataFrame(dates,index = None, columns = ["Date", "Value"])
df.to_csv("C:/Users/WilliamWilson/Documents/Outbox/YCharts_Cash.csv",index=False)
