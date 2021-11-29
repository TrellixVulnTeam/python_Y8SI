# example 
a = 10

# Assign value
b  = a 
# Add and assign value
b += a
print(b)

# Subtract and assign value
b -= a
print(b)

# multiply and assign
b *= a
print(b)

# divide and assign value '
b /= a
print(b)

# floor division and assign the value 
b //= a
print(b)

# modulo and assign the value 
b %=  a
print(b)


print('\nIDENTITY OPERATOR\n') 
# is and is not are identical operator:- both are use to check the value are located in same part of memory or not 
print('int')
a = 10
b  = 10
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

print('\nstring')
a = 'learncode '
b = 'learncode '
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

print('\nlist')
a = [1, 2]
b = [1, 2]
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

print('\nset')
a = {1, 2}
b = {1, 2}
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

print('\ntuple')
a =  (1, 2)
b =  (1, 2)
print(id(a))
print(id(b))
print(a is b)
print(a is not b)

# is operator :- Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
x = 5
if type(x) is int:
    print('condition is true')
else:
    print('Conditin is false')

# 'is not’ operator – Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
a = 5.5
if type(x) is not int:
    print('execute false')
else:
    print('execute true: because it is a float')

b  ='learncode'
if b is not'learncode':
    print('codition is false')
else:
    print('the condition is true')