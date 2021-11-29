# in and not in are the membership operator: they are use to test the value of variable in sequence 
# in operator is used to check the the is exists or not 
print('use of in operator') 
a = [1, 2]
b  = [1, 2]
print(2 in a)
print(1 in b)

list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8]
for items in list1:
    if items in list2:
        print(f'The list value is overlaped {list2}')
    else:
        print(f'the value are in order {list1}')

# not in operator 
x = 24
y = 20
list = [1, 20, 25, 3]
if x not in list:
    print(f'X value is 24 and is not present in list {list}')
    if y not in list:
        print(f'Y value is 20 and is present in list {list}')
    else:
        print(f'Y value is 20 and is present in list {list}') 
else:
    print(f'X value is 24 and is in list {list}')