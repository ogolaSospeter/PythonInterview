import sqlite3

# Connect to the database (creates a new database if it doesn't exist)
conn = sqlite3.connect('PythonInterview.sqlite')

cursor = conn.cursor()
sql_query = """CREATE TABLE  users (
    id integer PRIMARY KEY,
    username text NOT NULL,
    password text NOT NULL,
    email text NOT NULL,
    created_at text NOT NULL
    )
    """
cursor.execute(sql_query)