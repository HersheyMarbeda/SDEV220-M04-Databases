# # 16.3 Create a CSV file called books2.csv by using these lines:
# import csv
# import pandas

# book2 = [
#     ['title', 'author', 'year'],
#     ['The Weirdstone of Brisingamen', 'Alan Garner', 1960],
#     ['Perdido Street Station', 'China Miéville', 2000],
#     ['Thud!', 'Terry Pratchett', 2005],
#     ['The Spellman Files', 'Lisa Lutz', 2007],
#     ['Small Gods', 'Terry Pratchett', 1992],
# ]

# with open('book2.csv', 'w', newline='') as fout:
#     writer = csv.writer(fout)
#     writer.writerows(book2)
    
# df = pandas.read_csv('book2.csv')
# books = df.to_dict(orient='records')
# print(books)

# # 16.4 Use the sqlite3 module to create a SQLite database called books.db and a table called books 
# # with these fields: title (text), author (text), and year (integer).
# import sqlite3 

# connection = sqlite3.connect('books.db')
# cursor = connection.cursor()

# # Create the table
# cursor.execute('''
#     CREATE TABLE books (
#         title TEXT,
#         author TEXT,
#         year INTEGER
#     )
# ''')
# connection.commit() # commit the changes
# cursor.close()
# connection.close()


# # 16.5 Read books2.csv and insert its data into the book table.
# import csv
# import sqlite3

# connection = sqlite3.connect('books.db')
# cursor = connection.cursor()

# with open('book2.csv', 'r') as fin:
#     reader = csv.reader(fin)
#     # Skip the header row
#     next(reader)
#     for row in reader:
#         cursor.execute('''
#             INSERT INTO books (title, author, year)
#             VALUES (?, ?, ?)
#         ''', row)
# connection.commit()
# cursor.close()
# connection.close()

# # 16.6 Select and print the title column from the book table in alphabetical order.
# connection = sqlite3.connect('books.db')
# cursor = connection.cursor()

# cursor.execute('''
#     SELECT title FROM books ORDER BY title
# ''')

# for row in cursor.fetchall():
#     print(row[0])
    
# cursor.close()
# connection.close()

# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in 
# exercise 16.4. As in 16.6, select and print the title column 
# from the book table in alphabetical order.

from sqlalchemy import create_engine, MetaData, Table, select

# Connect to the SQLite database
# it's importatnt to use the correct path to the database file
engine = create_engine('sqlite:///books.db')
connection = engine.connect()
metadata = MetaData()

# Reflect the books table
books_table = Table('books', metadata, autoload_with=engine)

# Query to select and order the titles alphabetically
query = select(books_table.c.title).order_by(books_table.c.title)

# Execute the query and print the results
result = connection.execute(query)

print("\nTitles in alphabetical order:")
for row in result:
    print(row.title)

# Close the connection
connection.close()
