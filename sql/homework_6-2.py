# Homework 6-2

import sys
import sqlite3

def printrows(rows, title=None):
    if title:
        print('\n\n{}:\n'.format(title))
    for r in rows:
        print(', '.join(['{}']*len(r)).format(*r))


def main():
    with sqlite3.connect("cars.db") as conn:
        c = conn.cursor()
        
        data = [
            ('Ford', 'Focus', 500),
            ('Ford', 'Taurus', 1000),
            ('Honda', 'Civic', 1000),
            ('Honda', 'Accord', 1000),
            ('Ford', 'Explorer', 5000),
        ] 
        c.executemany("INSERT INTO inventory VALUES (?, ?, ?)", data)
        
        data = [
            ('Ford', 'Focus', 9999),
            ('Honda', 'Civic', 9999),
        ]
        c.executemany("UPDATE inventory SET Quantity = ? WHERE Make = ? AND Model = ?", data)
        
        c.execute("SELECT * FROM inventory")
        rows = c.fetchall()
        printrows(rows, 'Inventory')
        
        c.execute("SELECT * FROM inventory WHERE Make = 'Ford'")
        printrows(c.fetchall(), 'Just the Fords!')
        

if __name__ == '__main__':
    main()
    sys.exit(0)
