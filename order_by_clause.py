from connect import db1

cursor = db1.cursor()


cursor.execute("use books")

STATEMENT = """
    SELECT * FROM book ORDER BY id ASC

"""

cursor.execute(STATEMENT)

for r in cursor.fetchall():
    print(r)
