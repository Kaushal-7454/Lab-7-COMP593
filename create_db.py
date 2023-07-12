"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import sqlite3
from datetime import datetime

con = sqlite3.connect('social_network.db')
cur = con.cursor()
# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
    # TODO: Create function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    create_ppl_tbl_query = """
        CREATE TABLE IF NOT EXISTS people
            (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            province TEXT NOT NULL,
            bio TEXT,
            age INTEGER,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL
            );
            """
    cur.execute(create_ppl_tbl_query)
    con.commit()

    con.close()
    # Hint: See example code in lab instructions entitled "Creating a Table"
    return

def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Inserting Data into a Table"
    # Hint: See example code in lab instructions entitled "Working with Faker"
    add_person_query = """
        INSERT INTO people
        (
        name,
        email,
        address,
        city,
        province,
        bio,
        age,
        created_at,
        updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
# Define a tuple of data for the new person to insert into people table
# Data values must be in the same order as specified in query
    new_person = ('Kaushakumar Limbachiya',
'kaushal.@limbachiya.net',
'101, crawford drive',
'peterbourough',
'Ontario',
46,
'I am a introvert person who use keep silent everytime',
datetime.now(),
datetime.now())
# Execute query to add new person to people table
    cur.execute(add_person_query, new_person)
    con.commit()
    con.close()
    return

if __name__ == '__main__':
   main()