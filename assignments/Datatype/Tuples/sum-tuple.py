# python program to find the sum of the tuples
def sumTuple(a):
    '''this function is used to sum up the tuple'''
    ans = sum(a)
    return ans

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = sumTuple(a)
print(f'sum of the tuple is {b}')
print(sumTuple.__doc__)