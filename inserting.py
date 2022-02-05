from connect import db1

cursor = db1.cursor()
cursor.execute("use books")

INSERT_STATEMENT = """
    INSERT INTO book
    (title,isbn,author)
    values 
    ("learn django", "W.S Vincent", "odfmqowmdpoqwmdpomqw")   
"""

cursor.execute(INSERT_STATEMENT)
db1.commit()
