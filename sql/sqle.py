# INSERT comand with error handler

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()
    
    try:
        c.execute("""INSERT INTO populations VALUES('New York CIty', 'NY',
                       8200000)""")
        c.execute("""INSERT INTO populations VALUES('San Francisco', 'CA',
                    800000)""")
        
        c.commit()
    except sqlite3.OperationalError as e:
        print('Uh oh, something went wrong!\n\t{}'.format(e.message))
