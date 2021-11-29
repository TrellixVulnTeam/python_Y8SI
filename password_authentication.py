# password authentication 

import getpass # importing model 
database = {'yogesh.khanal':'123', 'khanal.yogesh':'456'} # creating a dictionary and storing keys and value 
username = input('Enter your name: ') # userinput for username 
password = getpass.getpass('Enter your password: ') # userinput for password
for i in database: # chicking (iterating) the database 
    if username == i: #condition
        print('user id is varifi ed!') # True
        while password != database.get(i): #condition 
            password = getpass.getpass('Wrong password!.... Enter your passwod again: ') # False 
        break 
    else:
        print('user id is not in database record!')
        break