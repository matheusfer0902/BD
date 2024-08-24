import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='pingo0902',
    database='livraria',
)

cursor = connection.cursor()