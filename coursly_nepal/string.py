# hello = 'python beginers course'
# print(hello[0:]) # print all the characters from position 0 to end
# print(hello[0]) # print first character
# print(hello[0:5]) # print character from position 0 to 5
# print(hello[:]) # print all the characters
# print(hello[-1]) # print last one character
# welcome = hello[:] # print all the characters that is in hello
# print(welcome)

# hey = 'yogesh'
# print(hey[1:-1]) # exclude first and last character

# ------>  string functions <----------
# course = 'this is python course provides by YOGESH'
# up_case = course.upper() # convert to uppercase
# lwr_case = course.lower() # convert to lower case
# find = course.find('H') # find the position of character, which is case sensative,
# replace = course.replace('provides', 'which is presentated') # replace function of string are also case sensative
# print(up_case)
# print(lwr_case)
# print(f"'H' is a position {find}")
# print(replace)


# # -------> use of in operator <----------
# update = 'this is string class'
# print('class' in update) # must return True or False, they are case sensative
# title = update.title() # it makes begining characters capital
# print(title)


# # ---------> arthematic operator <------------
# import math
# x = 3.5
# print('this i will roundup the float value and make it int ', round(x)) # it will roundup the value and make it 4
# print('when we use negative sign in abs (absolute) it always returns a positive number that is ',abs(-3.4)) # abs stand for absolute which always returns a positiove value

# celing and floor function
# print(math.ceil(2.5)) # ceil means celing which increment the value and make it int
# print(math.floor(2.5)) # it decrement the value and convert to int

# copy sign function
# a = 2
# b = -20
# c = 20.545
# d = 8
# print(math.copysign(a, b)) # it returns a first value and sign of second value
# print(math.fabs(b))  # returns a absolute value (positive)
# print(math.factorial(a)) # it only receive a positive value and work on 10*9+10*8+10*7.....10*0
# print(math.lcm(a, d)) # returns a lcm of two different number


# --------> if else condition <----------
# name = input("Enter your name: ")
# if len(name) < 3:
#     print('Name must be atleast 3 character')
# elif len(name) > 50:
#     print('Name must not be greater than 50 character')
# else:
#     print('Name is perfect!')

# weight = float(input('Enter your weight: '))
# print('a. pound')
# print('b. kilogram')
# opt = input('choose ur option: ')

# if opt.upper() == "A":
#     a = weight * 0.45359237
#     print(f'your weight in pound is {a}')
# elif opt.upper() == "B":
#     a = weight / 0.45
#     print(f'your weight in kg is {a}')
# else:
#     print('invalid choice!')


# -------------> while loop <----------------
# number gussing game
# secret_number = 10
# limit_option = 3
# guess_count = 0
# while guess_count < limit_option:
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('you won!')
#         break
# else:
#     print('sorry, you lose!')

# car game
# start = 'Start - to start the car'
# stop = 'Stop - to stop the car'
# ex_q = 'quit - to exit the game'
# started = False
# while True:
#     intake = input('> ').upper()
#     if intake == 'HELP':
#         print(f'{start} \n{stop} \n{ex_q}')
#     elif intake == 'START':
#         if started:
#             print('car is already started!')
#         else:
#             started = False
#             print('car start, ready to go!')
#     elif intake == 'STOP':
#         if not started:
#             print('car is already stoped!')
#         else:
#             started = False
#             print('Car stop!')
#     elif intake == 'QUIT':
#         break
#     else:
#         print('i dont understand the command...')


# ------------> for loop <----------------
# # list of list
# value = [["yogesh", 1], ["mahesh", 2], ["kusal", 3], ["dikshya", 4], ["ajaya", 5], ["bisal",6]]
# dictionary = dict(value) # typecasting the list in dictionary
# # print(dictionary)
# for name, item in dictionary.items(): # this is to print the dictionary value from the loop
# # for name, item in value:
#     print(name, item)

# # range function 
# for item in range(1, 10, 2): # this is to print the numbers from 1 -10 in difference of 2
#     print(item)

#  practice 
# cost = [10, 20, 50, 40, 60]
# total= 0
# for item in cost:
#     total += item
# print(f"Total: {total}")    
