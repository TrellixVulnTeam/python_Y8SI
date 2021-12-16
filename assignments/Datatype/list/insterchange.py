# Python program to interchange first and last elements in a list

def interchange(list1):
    '''Python program to interchange first and last elements in a list'''
    list1[0],list1[-1] = list1[-1],list1[0]
    # list at index[0] and list at index[-1] is swaped with list at index[-1] and with list at index[0]
    return list1

a = interchange(list1 = [12, 35, 9, 56, 24])
print(a)
print(interchange.__doc__)
