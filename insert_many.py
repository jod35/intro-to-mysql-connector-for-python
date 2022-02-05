from connect import db1

cursor = db1.cursor()

INSERT_STATEMENT = """
    INSERT INTO book (title,isbn,author) values (%s,%s,%s)
"""

values = [
    ("MySQL Connector/Python Revealed:", "Jesper Wisborg Krogh", "qdmqwopmdpmqwpdom"),
    ("MySQL Connector/Python Revealed:", "Jesper Wisborg Krogh", "qdmqwopmdpmqwpdom"),
    ("MySQL Connector/Python Revealed:", "Jesper Wisborg Krogh", "qdmqwopmdpmqwpdom"),
    ("MySQL Connector/Python Revealed:", "Jesper Wisborg Krogh", "qdmqwopmdpmqwpdom"),
]

cursor.execute("use books")

cursor.executemany(INSERT_STATEMENT, values)

db1.commit()
