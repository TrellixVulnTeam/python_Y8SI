# python program to find the sum of elements in lists 
def sum(list1):
    '''sum of the elements in list with for loop'''
    sum  = 0
    for i in list1:
        sum += i
    return sum

a = sum(list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(sum.__doc__)
print(f'sum of the list is: {a}') 


# def sum1(list2):
#     '''sum of the elements in list woth enumerate'''
#     sum = 0
#     for i, v in enumerate(list2): # this functions gives one 
#         sum += i
#     return sum

# a = sum1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(sum.__doc__)
# print(a)