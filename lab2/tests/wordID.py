import sqlite3
import string
import numpy as np
import copy
from collections import defaultdict

# Execute a simple query to find word ID from database file.

def dbExaminer (keyword):
    con = sqlite3.connect('dbFile.db')
    cursor = con.cursor()
    result=''
    cursor.execute('''SELECT wordID FROM lexicon_table WHERE (word = ?)''', [keyword])
    rows = cursor.fetchall()
    print rows

    con.commit()
    con.close()
    return result

dbExaminer('homepage')
