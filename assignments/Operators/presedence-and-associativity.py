# example 
# and have high presidence and tit will be checked at first 
name = 'learncode'
age = 0
if name == 'learncode' or name == 'python' and age >= 0:
    print('the codeition is true becasue the associativity of operators is from left to right.')
else:
    print('the condition is false because the operator is not working accordingly')

# operator associativity 
# left to right 
a = 100 / 10 * 1.9 
# (100/10) * 1.9
# 10 * 1.9
print(a)

b = 5 - 2 + 3
print(b)

c  = 5 -(2 + 3) # PARENTHEASIS have highest presidence 
print(c)

# right to left (exponential)
print(2 ** 3 ** 2)
# 2**3 = 8
# 8*8 = 64, 64*8 = 512

# expression 
exp = 100 + 200 / 10 - 3 * 10
print(exp)

x = 6
y = 2
print(x >= 2 or (x/y) > 2) #true 


x = 1
y = 0
print(x >= 2 and (x/y) > 2) # false 

# x = 6
# y = 0
# print(x >= 2 and (x/y) > 2) #error

# differecnce between is and == 
# equalitary operator compare the value of two different variable, where is check weather the bothe operands are located in same memory or not 

list1 = []
list2 = []
list3=list1

if (list1 == list2): #  true
    print("True")
else:
    print("False")

if (list1 is list2): # false 
    print("True")
else:
    print("False")

if (list1 is list3): # true 
    print("True")
else:
    print("False")

list3 = list3 + list2
if (list1 is list3): # false 
    print("True")
else:
    print("False")

x = 1
y = 0
print(x >= 2 and y != 0 and (x/y) > 2) # false 

x = 6
y = 0
print(x >= 2 and y != 0 and (x/y) > 2) # false