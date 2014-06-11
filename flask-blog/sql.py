# sql.py - Create SQLite3 table and populate with data

import sqlite3

with sqlite3.connect("blog.db") as conn:
    c = conn.cursor()
    
    # Create the table
    c.execute("CREATE TABLE posts (title TEXT, post TEXT)")
    
    # Insert dummy data
    data = [
        ("Good", "I'm good."),
        ("Well", "I'm well."),
        ("Excellent", "I'm excellent."),
        ("Okay", "I'm okay."),
    ]
    c.executemany('INSERT INTO posts VALUES(?, ?)', data)
