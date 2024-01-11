import sqlite3

# Connect to the database
conn = sqlite3.connect('chinook.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT name From sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")

# Fetch the results
results = cursor.fetchall()

# Do something with the results
for row in results:
    print("Table Name: ", row[0])
    cursor.execute(f"PRAGMA table_info('{row[0]}')")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]
    print("Column Name: ", column_names)

    chosen_column = 'NewColumn'  # Replace with the actual column name

    # Execute a query to get content of the chosen column
    cursor.execute(f"SELECT {chosen_column} FROM {row[0]}")
    
    # Fetch the results
    column_content = cursor.fetchall()

    # Print the content of the chosen column
    print(f"{chosen_column} content: {column_content}")
    print()

# Close the connection
conn.close()
