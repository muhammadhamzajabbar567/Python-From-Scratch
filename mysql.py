import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "m_hamza_jabbar",
    password = "hamza123"
)
print(mydb)