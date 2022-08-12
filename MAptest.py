import geopandas as gpd
import folium
import json

center = (51.3823, -2.3512)
Bath_map = folium.Map(location=center, zoom_start=13)

# gpd.read_file("Charging_Order_Boundary.shp").to_file('data.geojson', driver='GeoJSON')
caz_bound = "newdata.geojson"

geo_bound = json.load(open(caz_bound))

layer = folium.GeoJson(data=geo_bound, name='Clean Air Zone').add_to(Bath_map)


folium.LayerControl().add_to(Bath_map)
Bath_map.fit_bounds(layer.get_bounds())
Bath_map.save(outfile="Test_caz_3.html")
