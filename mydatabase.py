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
