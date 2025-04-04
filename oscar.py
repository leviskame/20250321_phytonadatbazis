import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)
mycursor = mydb.cursor()

#1.feladat
database = "oscar"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS oscar{database}")

#2.feladat
mycursor.execute(f"USE {database}")

mycursor.execute("SELECT ev, cim FROM film WHERE nyert = TRUE ORDER BY ev;")
for x in mycursor:
    print(x)

#3.feladat
mycursor.execute("SELECT ev FROM film GROUP BY ev HAVING COUNT(*) >= 10;")
for x in mycursor:
    print(x)

#4.feladat
mycursor.execute("SELECT cim FROM film WHERE ev BETWEEN 1939 AND 1945 AND bemutato IS NOT NULL;")
for x in mycursor:
    print(x)

#5.feladat
mycursor.execute("SELECT cim FROM film WHERE nyert = TRUE AND bemutato > DATE_ADD(STR_TO_DATE(CONCAT(ev, '-01-01'), '%Y-%m-%d'), INTERVAL 10 YEAR);")
for x in mycursor:
    print(x)

#6.feladat
mycursor.execute("SELECT keszito.nev, COUNT(film.id) AS jelolesek_szama, DATEDIFF(MAX(film.ev), MIN(film.ev)) AS elmult_ido FROM keszito JOIN kapcsolat ON keszito.id = kapcsolat.keszitoid JOIN film ON kapcsolat.filmid = film.id GROUP BY keszito.id HAVING COUNT(film.id) > 1;")
for x in mycursor:
    print(x)

#7.feladat
mycursor.execute("SELECT DISTINCT keszito.nev FROM keszito JOIN kapcsolat ON keszito.id = kapcsolat.keszitoid JOIN film ON kapcsolat.filmid = film.id WHERE film.id IN (SELECT filmid FROM kapcsolat WHERE keszitoid = (SELECT id FROM keszito WHERE nev = 'Clint Eastwood'));")
for x in mycursor:
    print(x)

#8.feladat
mycursor.execute("SELECT keszito.nev FROM keszito JOIN kapcsolat ON keszito.id = kapcsolat.keszitoid JOIN film ON kapcsolat.filmid = film.id WHERE film.bemutato IS NULL GROUP BY keszito.id HAVING COUNT(film.id) = 1;")
for x in mycursor:
    print(x)


mydb.commit()