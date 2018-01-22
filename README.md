# web-map

Web-Map using Python 3 and Folium

featuring

volcanoe spot in US with CircleMaker with different colors based on:
if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
        
population retrieved from 2005 data, world.json and displaying 
different colors based on population:
green < 10,000,000
orange if population is <= and < 20,000,000
red if population is greater than 20,000,000

Must install folium and pandas in project folder in order to run:
- pip3 install folium
- pip3 install pandas

Initalize the app by running in terminal: 
python3 map1.py



![screen shot 2018-01-22 at 11 17 51 am](https://user-images.githubusercontent.com/19434464/35236830-ed3dda10-ff65-11e7-98ce-9f3752f2858d.png)






