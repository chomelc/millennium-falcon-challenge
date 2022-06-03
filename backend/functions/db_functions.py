import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ Create a database connection to the SQLite database
    specified by the `db_file`.
    @param `db_file`: database file
    @return `Connection` object or `None`
    """
    cnx = None
    try:
        cnx = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return cnx


def select_all_routes(cnx):
    """
    Query all rows in the ROUTES table.
    @param `cnx`: the `Connection` object
    @return the fetched routes
    """
    cur = cnx.cursor()
    cur.execute("SELECT * FROM ROUTES")

    return (cur.fetchall())
