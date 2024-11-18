import csv
import pandas as pd

print("\n")
books = [
    ['author', 'book'],
    ['J.R.R. Tolkien', 'The Lord of the Rings'],
    ['Lynne Truss', 'Eats, Shoots & Leaves'],
]

# Write the books list to a CSV file
with open('books.csv', 'w', newline='') as fout:
    writer = csv.writer(fout)
    writer.writerows(books)

# Read the CSV file into a DataFrame
df = pd.read_csv('books.csv')

# Convert the DataFrame to a list of dictionaries
authors = df.to_dict(orient='records')

print(authors)