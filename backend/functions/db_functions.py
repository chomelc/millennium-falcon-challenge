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
        print(f'error: {e}')

    return cnx


def select_all_routes(cur):
    """
    Query all rows in the ROUTES table.
    @param `cur`: the `Connection`\'s cursor'
    @return the fetched routes
    """
    cur.execute("SELECT * FROM ROUTES")

    return (cur.fetchall())


def select_all_unique_planets(cur):
    """
    Query all unique planets in the ROUTES table.
    @param `cur`: the `Connection`\'s cursor'
    @return the names of the distinct planets
    """
    cur.execute(
        "SELECT DISTINCT origin FROM ROUTES UNION SELECT DISTINCT destination FROM ROUTES")

    return (cur.fetchall())
