from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password = "",
                                 host='127.0.0.1',
                                 database='kiralyok')

#tablak megjelenitese
cursor = cnx.cursor()
cursor.execute("SHOW TABLES")
for table in cursor: 
    print(table)

print("_______________________________________________________________________")

#uralkodok megjelenitese
cursor.execute("SELECT * FROM uralkodo")
for uralkodo in cursor: 
    print(uralkodo)

print("_______________________________________________________________________")

#kivalasztas
cursor.execute("SELECT * FROM uralkodo WHERE uralkodo.nev = 'I. Mátyás'")
for uralkodo in cursor: 
    print(uralkodo)
    
print("_______________________________________________________________________")

#
cursor.execute("SELECT szul,hal FROM uralkodo WHERE uralkodo.nev = 'I. Mátyás'")
for uralkodo in cursor: 
    print(f"Mátyás király élt: {uralkodo[0]} - {uralkodo[1]}")


cnx.close()
