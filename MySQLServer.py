import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="new"
)

mycursor = mydb.cursor()

# Create a table named `customers` (if it doesn't exist)
try:    
    mycursor.execute("""
    CREATE DATABASE IF NOT EXISTS alx_book_store
    """)
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error:
    print("ERROR")

mydb.commit()
mycursor.close() 
mydb.close()