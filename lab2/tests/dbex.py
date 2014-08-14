import sqlite3
import string
import numpy as np
import copy
from collections import defaultdict

# The examiner tests the database entries and tries to find word from lexicon table.
# Once a word is found, the pagerank of the docid, and its url is returned to terminal,
# along with the wordID, just in case.

def dbExaminer (query):
    con = sqlite3.connect('dbFile.db')
    cursor = con.cursor()
    result=''
    # SELECT PageRank.ranking, DocIndex.url, Lexicon.wordID, InvertedIndex.docID
    cursor.execute('''SELECT PageRank.ranking, DocIndex.url, Lexicon.wordID, InvertedIndex.docID FROM Lexicon
    INNER JOIN InvertedIndex
        ON Lexicon.wordID = InvertedIndex.wordID
    INNER JOIN DocIndex
        ON InvertedIndex.docID = DocIndex.doc_ID
    INNER JOIN PageRank
        ON DocIndex.doc_ID = PageRank.docID
    WHERE Lexicon.word = ?
    ORDER BY ranking DESC''', [query]);
    # Rank result from high to low.
    # con.commit() , url ASC
    rows = cursor.fetchall()
    # print rows
    for row in rows:
        result += 'PageRank:%s %s %s %s' % (str(row[0]), (row[1]), str(row[2]), str(row[3]))
    con.close()
    return result

# Print to terminal and see what we got.
print dbExaminer('instructor')
