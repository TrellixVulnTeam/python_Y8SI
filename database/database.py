# database 

import sqlite3
# connecting to database 
connection = sqlite3.connect("my_database.db")

# cursor 
crsr = connection.cursor()

# SQL commanda to create a table 
sql_commands = '''CREATE TABLE sample (
    sid INTEGER PRIMARY KEY, 
    fname VARCHAR(20), 
    lname VARCHAR(20), 
    course_name VARCHAR(20),
    gender VARCHAR(1), 
    join_data DATE
    );'''

# execute the statements  
crsr.execute(sql_commands)

# SQL commands to insert data in table 
sql_commands = '''INSERT INTO sample VALUES (1, "Yogesh", "Khanal", "python", "M", "31/12/2021");'''
crsr.execute(sql_commands)
connection.commit()

sql_commands = '''INSERT INTO sample VALUES (2, "Ramesh", "Thapa", "python", "M", "31/12/2021");'''
crsr.execute(sql_commands)
connection.commit()

sql_commands = '''INSERT INTO sample VALUES (3, "ujjwol", "Thapa", "Java", "m", "31/12/2021");'''
crsr.execute(sql_commands)
connection.commit()


# fetching data 
crsr.execute('SELECT * FROM sample')
# store all fetch data in result variable 
result = crsr.fetchall()

print(type(result))

# since we have already selected all the data entries using "SELECT *" SQL command and stored then in the ans variable, all we need to do now is to print out result variable 
# for i in result:
    # print(i)

print(result[0])


# if there is no error the following line will execute 
print('Connection is successfull.')
