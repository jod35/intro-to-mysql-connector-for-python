import mysql.connector

connection_args = {"host": "localhost", "user": "jod35", "password": "nathanoj35"}

db1 = mysql.connector.connect(**connection_args)

print(db1.connection_id)

db2 = mysql.connector.connect(**connection_args)

print(db2.connection_id)

db2.close()

db3 = mysql.connector.connect(**connection_args)
print(db3.connection_id)

db3.close()
