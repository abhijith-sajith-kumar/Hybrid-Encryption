import numpy as np
from Functions import Fnctn
from Crypto import encrypt, decrypt
import sqlite3

# connect to SQLite database
conn = sqlite3.connect("C:/Users/abhij/Desktop/DBMS_/chinook.db")
cursor = conn.cursor()

# Retrieve all data from the database
cursor.execute("SELECT name From sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print("Table Name: ", table_name)

    cursor.execute(f"PRAGMA table_info({table_name});")
    columns = cursor.fetchall()
    new_column_exists = any(column[1] == 'NewColumn' for column in columns)

    if not new_column_exists:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN NewColumn TEXT;")

        # Retrieve data from the table
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    
# Encryption Algorithm
    enc_data = []
    for row in data:
        text = row[0]
        list1 = [ord(i) for i in str(text)]
        obj = Fnctn(len(list1))
        x = obj.nrst_sqrt(len(list1))
        filled = obj.arr_fill(len(list1), list1)
        arr = np.array(filled)
        new = arr.reshape(x,x)
        crypt = encrypt()
        z,k1,k2,k3 = crypt.sub_cipher(new)
        sub, k4 = crypt.pos_cipher(z)
        y = crypt.enc_txt(sub)
        # print("Encrypted Text", y)
        enc_data.append(tuple([y] + [row[0]]))


    column_names = [column[1] for column in cursor.description]
    update_statement = f"UPDATE {table_name} SET NewColumn = ? WHERE {cursor.description[0][0]} = ?"


    if enc_data:
        print("Update Statement", update_statement)
        # print("encrypted data", enc_data)
        cursor.executemany(update_statement, enc_data)
        conn.commit()


conn.close()