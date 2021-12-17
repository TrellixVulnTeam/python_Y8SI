# python program to find a size of Tuple 
def sizeTuple(x):
    '''this function is use to check the length of tuple'''
    ans = len(x)
    return ans

x = (1, 2, 3, 4, 'hello', 'python', 'developers', 10, 20)
a = sizeTuple(x)
print(f'size of tuple is {a}')
print(sizeTuple.__doc__)