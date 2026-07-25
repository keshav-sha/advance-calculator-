import sqlite3
# here we are importing the sqlite3 module, which provides a lightweight disk-based database that doesn't require a separate server process. 
# It allows us to create and interact with SQLite databases in Python.

DATABASE_NAME = "history.db"
# here we are defining a constant variable DATABASE_NAME and assigning it the value "history.db".

def get_connection():
    return sqlite3.connect(DATABASE_NAME)
# here we are defining a function called get_connection that establishes a connection to the SQLite database specified by the DATABASE_NAME variable.

def initialize_database():
# here we are defining a function called initialize_database that initializes the database by creating a table called "history" if it does not already exist.

    conn = get_connection()
    cursor = conn.cursor()
# here we are creating a cursor object from the database connection. 
# The cursor is used to execute SQL commands and queries on the database.

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            operation TEXT NOT NULL,

            input TEXT NOT NULL,

            result TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)
# here we are executing an SQL command to create a table called "history" if it does not already exist.
# The table has the following columns:

    conn.commit()
    conn.close()
# here we are committing the changes to the database and closing the connection.