# UPDATE and DELETE

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()
    
    c.execute("""
                UPDATE population 
                SET population = 9000000
                WHERE city='New York City'
                """)
    c.execute("DELETE FROM population WHERE city='Boston'")

    c.execute("SELECT * FROM population")
    print('\nNew Data:\n')    
    rows = c.fetchall()
    for r in rows:
        print(', '.join(['{}']*len(r)).format(*r))
