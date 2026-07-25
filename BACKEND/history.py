from database import get_connection
# here we are importing the get_connection function from the database module.
# it is used to establish a connection to the SQLite database specified by the DATABASE_NAME variable in the database module.

class History:

    @staticmethod
    def save(operation, user_input, result):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            INSERT INTO history
            (operation,input,result)

            VALUES(?,?,?)

        """, (operation, user_input, str(result)))

        conn.commit()

        conn.close()
# here we are defining a static method called save that takes three parameters: operation, user_input, and result.
# It establishes a connection to the SQLite database using the get_connection function, creates a cursor object

    @staticmethod
    def get_all():

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            SELECT *

            FROM history

            ORDER BY id DESC

        """)

        rows = cursor.fetchall()

        conn.close()

        return rows
# here we are defining a static method called get_all that retrieves all records from the "history" table in the SQLite database.
# It establishes a connection to the database, creates a cursor object, executes an SQL query to select all records from the "history" table ordered by id in descending order, fetches all the rows, closes the connection, and returns the fetched rows.

    @staticmethod
    def delete(record_id):

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            DELETE FROM history

            WHERE id=?

        """, (record_id,))

        conn.commit()

        conn.close()
# here we are defining a static method called delete that takes a parameter record_id.
# It establishes a connection to the SQLite database, creates a cursor object, executes an SQL query

    @staticmethod
    def clear():

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("""

            DELETE FROM history

        """)

        conn.commit()

        conn.close()
# here we are defining a static method called clear that deletes all records from the "history" table in the SQLite database.
# It establishes a connection to the database, creates a cursor object, executes an SQL query to delete all records from the "history" table, commits the changes, and closes the connection.