from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd

canada_east = 25.466838
canada_west = 25.464684
canada_north = 65.058998
canada_south = 65.058421
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

final_df = pd.read_csv("./data/finaldata.csv")
sensors_locations_df = pd.read_csv("./data/SensorsLocation.csv")
latitudes = sensors_locations_df["Latitude"]
longitudes = sensors_locations_df["Longitude"]
fig = plt.figure(figsize=(19.2, 10.8))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([canada_west, canada_east, canada_south, canada_north])
ax.scatter(longitudes, latitudes, color="#0000ff", s=2)
ax.stock_img()
for index, row in final_df.iterrows():
    txt = ax.text(0.05, 0.95, row["date"], transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
    sensorheatmap = ax.scatter(row["Longitude"], row["Latitude"],
               color="#ff0000", s=row["pir"] / 10)
    plt.savefig("./images/" + str(index) + ".png")
    txt.remove()
    sensorheatmap.remove()



# ax.set_extent([-100, 100, 0, 80], crs=ccrs.PlateCarree())
# plt.show()
# ax.background_img(name='./data/BG.PNG', resolution='low')
# ax.scatter(longitudes, latitudes, final_df["pir"].iloc["0"],
#            color="#ff0000", alpha=0.8,
#            transform=ccrs.PlateCarree())
