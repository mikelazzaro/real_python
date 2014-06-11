# SELECT statement, convert unicode chars

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()

    c.execute("SELECT firstname, lastname FROM employees")
    rows = c.fetchall()
    for r in rows:
        print('{}, {}'.format(*r))
