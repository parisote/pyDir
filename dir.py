import geocoder
import mysql.connector

mydb = mysql.connector.connect(
  host="x",
  user="x",
  password="x",
  database="x"
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("SELECT p.person_id, p.last_name, p.first_name, ph.street, ph.number, ph.id FROM person_home ph LEFT JOIN person p ON p.default_home_id = ph.id WHERE ph.province_id = 'AR-C' AND ph.status = 'ENABLED' AND ph.id > 0 limit 0,100")

sql = "INSERT INTO person_home_lat_lon (person_id,person_name,lat,lon) VALUES (%s,%s,%s,%s)"
valA = []

for x in mycursor:
  dir = x[3] + " " + x[4] +" Buenos Aires, Argentina"
  name = x[1] + ", " + x[2]
  id = x[0]
  hId = x[5]
  loc = geocoder.osm(dir)
  if loc.latlng:
   val = (id,name,loc.latlng[0],loc.latlng[1])
   print(hId,val)
   valA.append(val)

mycursor.executemany(sql, valA)
mydb.commit()
print(mycursor.rowcount, "record insertados.")
   