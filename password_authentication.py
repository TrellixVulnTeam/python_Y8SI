# password authentication 
import getpass # it dpesnot show how the password that we enter 
import pwinput # when we enter a password it will comvert to astric 
# importing model 
database = {'yogesh':'123', 'khanal':'456'} # creating a dictionary and storing keys and value 
username = input('Enter your name: ') # userinput for username 
for i in database.keys():
    if username == i:
        # password = getpass.getpass("Enter your password: ")
        password = pwinput.pwinput("Enter your password: ")
        if password == database[i]:
            print('Account is activated!')
            break
        else:
            print("Password couldnot match!")
            break
    else:
        print('Username is not found!')
        break