import mysql.connector

cnx=mysql.connector.connect(host="localhost", user="root" ,password="")
mycursor=cnx.cursor()

query= ("SELECT *from Yemek_Tarifi")
mycursor.execute(query)
myresult= mycursor.fetchall()
 
for(yemekadi , malzemeler, yapilisi) in mycursor:
    print(yemekadi , malzemeler ,yapilisi);
    mycursor.close()
    cnx.close()
