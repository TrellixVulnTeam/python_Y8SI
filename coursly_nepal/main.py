# numbers 
# binary conversion 
x = 15
y = hex(x)
z = 0xf
print(y)
print(z)
print(oct(8))
print(bin(2))
# ---------> operators <---------------
# a = 5
# print(type('a')) # chicking an data type if an variable 

# a = b = c = 1
# print(a, b, c) # we can assign in this way too but while creating an memory in an device it will name as abc

# re-assignment 
# b = 4 # value of b will be update here 
# print(a, b, c)

# # keywords of py
# import keyword 
# print(keyword.kwlist)

# operator and operants 
# a, b = 4, 2
# sum =  a + b 
# a = a + b # 5 + 4 
# a += b # 9 = +4
# print(a) # 13

# c, d = 8.0, 2
# # print(a//b)
# # print(9%-2) # => 4.5=> 5 * 2=> 10 - 9 ==> 1 ans 

# # quotient, remainder
# e, f = divmod(12, 2)  # quotient, remainder in same line 
# print(e, f)


# # -----------> 
# a = 'hello\n'
# b = 'yogesh'
# c = a + b
# print(c)
# a = 'eh\b\b'
# print(a)

# x = 'hello \f welcome' # in windows it will print the female sign character 
# print(x) 

# y = 'hey welcome \ryogesh here' # it take all the value 
# # print(y)


# # --------------> input / output <-------------
# print(1, 2, sep='*') # it seperate the inputs with value keep inside the strin
# print(1, 2, 3, end='&') # at the end the end value will be attach
# print(1, 2, 3, 4, 5, sep = '*', end='&') 
# print('\n')

# # important 
# va = 5
# bal = 10
# print('the value of x is {} and value of y is {}'.format(va, bal))
# print('the value of x is {0} and value of y is {1}'.format(va, bal)) # here 0 and 1 represent the position of value that is in format

# # arguments
# print('hello {name}, {greeting}'.format(name = 'yogesh', greeting = "how are u?"))

# hello =  'hello guys...'
# abt = 'how are u doing ?'
# print(f'{hello}, {abt}') # this is very important (namely fstring )


# ----------> if/else coindition <----------
# a = "string"
# b = 5
# c = 4
# if a == 'string':
#     print("True")
# elif c < b:
#     print("true")
# else :
#     print("false")

# x = 2
# if x > 2:
#     print("yes")
# else :
#     print("no")