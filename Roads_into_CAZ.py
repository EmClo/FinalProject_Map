import json
import folium
import pandas as pd
center = (51.3823, -2.3512)
m = folium.Map(location=center, zoom_start=13)

data = pd.read_csv("Caz_road_Boundaries.csv")

for i in range(0,len(data)):
    folium.Marker(
        location=[data.iloc[i]['Latitude'], data.iloc[i]['Longitude']], popup=data.iloc[i]['Street_name'],).add_to(m)


folium.LayerControl().add_to(m)

m.save(outfile="Test_roads.html")