# Homework 6-2

import sys
import sqlite3


def main():
    with sqlite3.connect("cars.db") as conn:
        c = conn.cursor()
        
        c.execute("""
                    CREATE TABLE orders
                        (make TEXT, model TEXT, order_date DATE)
                    """)
        
        data = [
            ('Ford', 'Focus', '2014-01-02'),
            ('Ford', 'Focus', '2014-01-03'),
            ('Ford', 'Focus', '2014-01-04'),
            ('Ford', 'Focus', '2014-01-05'),
            ('Ford', 'Focus', '2014-01-06'), 
            ('Ford', 'Taurus', '2014-01-10'),
            ('Ford', 'Taurus', '2014-01-11'),
            ('Ford', 'Taurus', '2014-01-12'),
            ('Ford', 'Taurus', '2014-01-13'),
            ('Ford', 'Taurus', '2014-01-14'),
            ('Honda', 'Civic', '2014-01-15'),
            ('Honda', 'Civic', '2014-01-21'),
            ('Honda', 'Civic', '2014-01-22'),
            ('Honda', 'Civic', '2014-01-23'),
            ('Honda', 'Civic', '2014-01-24'),
            ('Honda', 'Accord', '2014-01-25'),
            ('Honda', 'Accord', '2014-01-29'),
            ('Honda', 'Accord', '2014-02-01'),
            ('Honda', 'Accord', '2014-02-02'),
            ('Honda', 'Accord', '2014-02-03'),
            ('Ford', 'Explorer', '2014-04-01'),
            ('Ford', 'Explorer', '2014-04-01'),
            ('Ford', 'Explorer', '2014-04-01'),
            ('Ford', 'Explorer', '2014-04-01'),
            ('Ford', 'Explorer', '2014-04-01'),

        ] 
        c.executemany("INSERT INTO orders VALUES (?, ?, ?)", data)
        
        
        c.execute("SELECT * FROM inventory")
        rows = c.fetchall()
        for make, model, _ in rows:
            c.execute("SELECT * FROM orders WHERE Make = '{}' AND Model = '{}'" \
                        "".format(make, model))
            orders = c.fetchall()
            printrows(orders, '{} {}'.format(make, model))

        

def printrows(rows, title=None):
    if title:
        print('\n\n{}:\n'.format(title))
    for r in rows:
        print(', '.join(['{}']*len(r)).format(*r))


if __name__ == '__main__':
    main()
    sys.exit(0)
