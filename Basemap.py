import geopandas as gpd
import pandas as pd
import geoplot as gplt
from cartopy import crs as ccrs
import matplotlib.pyplot as plt
import contextily as ctx
import folium

gpd.read_file("Charging_Order_Boundary.shp").to_file('data.geojson', driver='GeoJSON')