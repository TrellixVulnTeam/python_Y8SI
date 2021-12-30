# amount = 100000

# if (amount > 2000000)
# print('you are eligable to purchase a gold') 

# marks = 1000
# # perform devision with 0
# a =  marks /0
# print(a)

# # try and except 
# try:
#     # some code 
# except:
#     # executed if error in ths 
#     #  try block 

# working condition of try 
from typing_extensions import final


def division(x, y):
    try: 
        # floor division: vives fractional part of solution 
        retult = x // y
        print('yeah! your answer is: ', retult)
    except ZeroDivisionError:
        print('sorry ! you are divining by zero')

# look at the parameters and note working condition  
division(3, 2)

# demostrate working condition of try: 
def division(x, y):
    try: 
        # floor division: vives fractional part of solution 
        retult = x // y
        print('yeah! your answer is: ', retult)
    except ZeroDivisionError:
        print('sorry ! you are divining by zero')

# look at the parameters and note working condition  
division(3, 0)


# try: 
#     # some code 
# except: 
#     # execute is error in the  
#     # try block 
# else:
#     # execute if no execution

# program to depict clause with try-except 
# function which returns a /b
print()
def abc(a, b):
    try: 
        c = ((a/b) / (a-b))
    except ZeroDivisionError:
        print('a/b result in 0')
    else:
        print(c)

# driver program to test above function 
abc(2.0, 3.0)
abc(3.0, 3.0)


 # finally  syntax
# try: 
#     # some code 
# except:
#     # execte if error in the try block 
# else:
#     # execute if no exception 
# finally:
#     # coms code ....(always executed)

# python program to demostrate finally 
print()
try: 
    k = 5//0 # raise division error 
    print(k)
except ZeroDivisionError:
    print('can\'t divide by zero')
finally:
    # this block always execute 
    # regardless of execution generation 
    print('This line always executes!')