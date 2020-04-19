import pandas as pd
import datetime

target_date = datetime.datetime(2017, 9, 26)
i = 0
for chunk in pd.read_csv("./data/data.csv", chunksize=100):
    i += 1
    datetime_str = chunk["timestamp"].to_string().split()[1]
    datetime_object = datetime.datetime.strptime(datetime_str, '%Y-%m-%d')
    if(datetime_object > target_date):
        break
    if(i == 1):
        chunk.to_csv("./data/FirstThreeMonth.csv", index=None, mode='a')
    else:
        chunk.to_csv("./data/FirstThreeMonth.csv", index=None, mode='a', header=False)
