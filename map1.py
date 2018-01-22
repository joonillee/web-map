import folium
import pandas

# reading volcanoes txt file
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

# multiple color dots depends on elevation level
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# initial view 
map = folium.Map(location=[34, -85], zoom_start=5, tiles="Mapbox Bright")

# feature group volcanoes and population dropdown menu
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
# reading and displaying different colors depends on population as of 2015 json data
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

# popup marker where I am
map.add_child(folium.Marker(location=[34, -85], popup="Hey There. I am Atlanta.", icon=folium.Icon(color='green')))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

# funtion to update the html
map.save("Map1.html")
