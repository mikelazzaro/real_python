# Create SQLite3 database and table

import sqlite3

# Connect to db (auto-create if it doesn't exist)
conn = sqlite3.connect("new.db")

# Get cursor
cursor = conn.cursor()

# Drop table if it exists
cursor.execute("""
                DROP TABLE IF EXISTS population
                """)

# Create table
cursor.execute("""
                CREATE TABLE population
                    (city TEXT, state TEXT, population INT)
                """)

# Close the database
conn.close()
