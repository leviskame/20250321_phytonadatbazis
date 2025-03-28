import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)

mycursor = mydb.cursor()

#adatbazis letrehozasa
database = "mydatabases"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS mydatabases{database}")

#adatbazis mutatasa
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

#adatbazis hasznalata
mycursor.execute(f"USE {database}")

#costumers tabla letrehozasa
mycursor.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

#tabla mutatasa
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()


