from connect import db1


cursor = db1.cursor()


STATEMENT = """
 SELECT * FROM book LIMIT 2 OFFSET 1

"""
cursor.execute("use books")

cursor.execute(STATEMENT)

for r in cursor.fetchall():
    print(r)
