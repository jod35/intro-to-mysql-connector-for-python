from connect import db1

cursor = db1.cursor()

cursor.execute("CREATE DATABASE books")
