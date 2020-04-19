import pandas as pd
import datetime
import numpy as np
import numpy.random
import matplotlib.pyplot as plt


def sort_data_and_remove_hyphen():
    df = pd.read_csv("./data/FirstThreeMonth.csv")
    df = df.sort_values(by=['id', 'timestamp'])
    df["id"] = df["id"].replace('-', '', regex=True).astype(str)
    df.to_csv('./data/sorted.csv', index=None, mode='w')


def remove_unknown_sensors():
    df = pd.read_csv("./data/sorted.csv")
    sensors_locations_df = pd.read_csv("./data/SensorsLocation.csv")
    sensors_list = sensors_locations_df["Device ID"].astype(
        str).values.tolist()
    df = df[df['id'].str.lower().isin([x.lower() for x in sensors_list])]
    df.to_csv('./data/sorted.csv', index=None, mode='w')


def sum_up_each_hundered():
    i = 0
    for chunk in pd.read_csv("./data/sorted.csv", chunksize=100):
        i = i + 1
        # hour = pd.to_datetime(chunk['timestamp']).hour
        new_dataframe = pd.DataFrame(
            columns=["id", "timestamp", "date", "co2", "humidity", "light", "temperature", "pir"])
        first_date = pd.to_datetime(
            chunk['timestamp'].iloc[0], errors='coerce')
        last_date = pd.to_datetime(
            chunk['timestamp'].iloc[-1], errors='coerce')
        new_dataframe = new_dataframe.append({"id": chunk["id"].iloc[0], "timestamp": last_date - first_date, "date": last_date, "co2": chunk["co2"].mean(), "humidity": chunk["humidity"].mean(
        ), "light": chunk["light"].mean(), "temperature": chunk["temperature"].mean(), "pir": chunk["pir"].sum()}, ignore_index=True)
        if(i == 1):
            new_dataframe.to_csv(
                "./data/sortedperhundered.csv", index=None, mode='w')
        else:
            new_dataframe.to_csv(
                "./data/sortedperhundered.csv", index=None, mode='a', header=False)


def concat_lat_Lng_to_data():
    df = pd.read_csv("./data/sortedperhundered.csv")
    sensors_locations_df = pd.read_csv("./data/SensorsLocation.csv")
    new_df = pd.merge(df, sensors_locations_df, on="id", how='inner')
    print(new_df)
    new_df.to_csv("./data/finaldata.csv", index=None, mode='w')


# sort_data_and_remove_hyphen()
# remove_unknown_sensors()
sum_up_each_hundered()
concat_lat_Lng_to_data()
# # Create data
# x = np.random.randn(4096)
# y = np.random.randn(4096)

# # Create heatmap
# heatmap, xedges, yedges = np.histogram2d(x, y, bins=(64,64))
# extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# # Plot heatmap
# plt.clf()
# plt.title('Pythonspot.com heatmap example')
# plt.ylabel('y')
# plt.xlabel('x')
# plt.imshow(heatmap, extent=extent)
# plt.show()
