import sqlite3

connection = sqlite3.connect("data.db")


def create_table():
       with connection:
              connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")


def add_entry(entry_content, entry_date):
       with connection:
              # Not using f string here to avoid SQL injection attacks
              connection.execute(f"INSERT INTO entries VALUES (?,?);", (entry_content, entry_date))
    
def get_entries():
       # AS we are not commiting or rolling anything back from the database, therefore we done need the context manager i.e with conn...
       cursor = connection.execute("SELECT * FROM entries;")
       return cursor
       