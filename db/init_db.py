'''
Author: Derek R. Greene
Email: derek@derekrgreene.com

Description:
    Simple python script to initialize SQlite database. 
'''

import sqlite3, os

DB_PATH = 'PHI.db'

def init_db():
    '''
    Method to initialize database
    '''
    if not os.path.exists(DB_PATH):
        with sqlite3.connect(DB_PATH) as db:
            with open('schema.sql') as f:
                db.executescript(f.read())
        print("Database initialized.")


if __name__ == '__main__':
    init_db()
