# program to reverse a list 

def reverse(a):
    '''reverse a list ''' 
    a.sort(reverse = True)
    return a

b = reverse(a=[1, 8, 7, 9, 2, 3, 6, 7])
print(reverse.__doc__)
print('Reverse the list: ')
print(b)
