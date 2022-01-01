import sqlite3

try:
    serverConnection = sqlite3.connect('assignment1_Database.db')
    crsr = serverConnection.cursor()
    print('Database Created successfullt to SQLite server')
    print()

    # create a table 
    insert_query = """CREATE TABLE assignment1 (id INTEGER PRIMARY KEY, fname VARCHAR(20), lname VARCHAR(20))"""
    crsr.execute(insert_query)
    serverConnection.commit()
    print("Databse table is Created")

# inserting value into databes 
    insert_query = "INSERT INTO assignment1 VALUES (1, 'Ajaya', 'Rai')"
    crsr.execute(insert_query)
    serverConnection.commit()

# insert data into databse using forloop 
# primary key 
    id = [2, 3, 4, 5, 6]

# fname 
    fname = ['Bisal', 'Rawan', 'Bivishan', 'Dasarath']

# lname 
    lname = ['Kunwar', 'King','Maha-mantri', 'RoyalKing']


    for i in range(6):
        crsr.execute(
            f"INSERT INTO assignment1 VALUES ({id[i]}, '{fname[i]}', '{lname[i]}')")
        serverConnection.commit()

    # for i in range(5):
        # crsr.execute(
        # f'INSERT INTO welcome VALUES ({id[i]}, "{f_name[i]}", "{l_name[i]}")')
        # serverConnection.commit()

except sqlite3.Error as error:
    serverConnection.commit()
    print('Failed to insert data into database', error)
    print()

finally:
    if serverConnection:
        serverConnection.close()
        print('The SQLite connection is closed')
