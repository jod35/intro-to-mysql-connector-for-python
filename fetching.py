from connect import db1

cursor = db1.cursor()

cursor.execute("use books")

cursor.execute(
    """
    SELECT * FROM book
"""
)


result = cursor.fetchall()


for r in result:
    print(r)
