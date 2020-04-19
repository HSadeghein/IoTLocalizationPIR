from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import pandas as pd


final_df = pd.read_csv("./data/finaldata.csv")
sensors_locations_df = pd.read_csv("./data/SensorsLocation.csv")
latitudes = sensors_locations_df["Latitude"]
longitudes = sensors_locations_df["Longitude"]
fig = plt.figure(figsize=(19.2, 10.8))
ax = plt.axes(projection=ccrs.Mercator(central_longitude=25.465690, 
                                       min_latitude=-2,
                                       max_latitude=80))
# ax.set_extent([-20, 20, -20, 20], crs=ccrs.PlateCarree())
ax.coastlines()

plt.show()
# ax.background_img(name='./data/BG.PNG', resolution='low')
# ax.scatter(longitudes, latitudes, final_df["pir"].iloc["0"],
#            color="#ff0000", alpha=0.8,
#            transform=ccrs.PlateCarree())
