#pip install psycopg2-binary
import psycopg2
 
# Establishing the connection
connection = psycopg2.connect(
    database="livraria",
    user='postgres',
    password='root',
    host='localhost',
    port='5432'
)
 
# Creating a cursor object using the 
# cursor() method
cursor = connection.cursor()
