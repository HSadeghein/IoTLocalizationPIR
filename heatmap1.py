"""
File containing code to produce graphs, maps, and GIFs
"""

import pandas as pd
import gmplot
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


def heat_map():

    sensors_locations_df = pd.read_csv("./data/SensorsLocation.csv")

    # Store our latitude and longitude
    latitudes = sensors_locations_df["Latitude"]
    longitudes = sensors_locations_df["Longitude"]

    # Creating the location we would like to initialize the focus on.
    # Parameters: Lattitude, Longitude, Zoom
    gmap = gmplot.GoogleMapPlotter(
        65.058724, 25.465690, 20, apikey="AIzaSyDcReXXFibLBcWozq-BBFqSyub3W-o_0Io")

    # Overlay our datapoints onto the map
    gmap.heatmap(latitudes, longitudes, radius=2, opacity=1)
    gmap.heatmap(longitudes, latitudes, radius=3, opacity=0.5)

    # Generate the heatmap into an HTML file
    gmap.draw("tellus.html")


def map_scatter_plot():
    # Example taken from https://plotly.com/python/scatter-plots-on-maps/
    # Plotting locations of US airports

    df = pd.read_csv('./data/SensorsLocation.csv')

    fig = go.Figure(data=go.Scattergeo(
        lon=df['Longitude'],
        lat=df['Latitude']
    ))

    fig.update_layout(
        title='Most trafficked US airports<br>(Hover for airport names)',
        geo_scope='usa',
    )
    fig.show()


def bar_chart():
    # Example from https://pythonspot.com/matplotlib-bar-chart/

    objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    y_pos = np.arange(len(objects))
    performance = [10, 8, 6, 4, 2, 1]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.draw()
    plt.waitforbuttonpress(0) # this will wait for indefinite time
    plt.close()

def scatter_plot():
    # Example scatter plot with line joining each point

    x_data = np.arange(0, 10, 1)
    y_data = np.arange(0, 10, 1)

    fig = plt.figure()
    plt.scatter(x_data, y_data)  # scatter plot
    plt.plot(x_data, y_data)  # line graph
    plt.show()


if __name__ == "__main__":
    heat_map()
    # map_scatter_plot()
    bar_chart()
    scatter_plot()
