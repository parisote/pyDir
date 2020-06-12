import mysql.connector
import json

mydb = mysql.connector.connect(
  host="x",
  user="x",
  password="x",
  database="x"
)

geojson = {
    'type': 'FeatureCollection',
    'features': []
}

mycursor = mydb.cursor(buffered=True)
mycursor.execute("SELECT * FROM person_home_lat_lon")

for x in mycursor:
	geojson['features'].append({
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [x[3], x[4]],
                },
                "properties": {
                    "id": x[0],
                    "name": x[2]
                }
            })
			
with open('geo_results.geojson', 'w') as geofile:
    geofile.write(json.dumps(geojson, indent=2))