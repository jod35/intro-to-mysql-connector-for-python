from connect import db1


cursor = db1.cursor()


cursor.execute("Use books")

TABLE_STATEMENT = """

CREATE TABLE book(
    id int auto_increment,
    title varchar(45),
    isbn text,
    author varchar(40),
    primary key (id)
)

"""

cursor.execute(TABLE_STATEMENT)
