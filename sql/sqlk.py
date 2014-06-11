# JOINing data

import sqlite3

with sqlite3.connect("new.db") as conn:
    c = conn.cursor()
    
    c.execute("""
                SELECT 
                    population.city, 
                    population.population,
                    regions.region
                FROM 
                    population, 
                    regions 
                WHERE population.city = regions.city
                """)
    
    rows = c.fetchall()
    for r in rows:
        print(', '.join(['{}']*len(r)).format(*r))
