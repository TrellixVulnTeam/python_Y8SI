# python program to count occurances of an elements in list 
def count(list1, c):
    '''function to count the occurance of elemenst in list'''
    ans = list1.count(c)
    return ans

list1 = [4, 5, 4, 5, 1, 2, 3, 5, 4, 1, 5, 87]
c = 4
a = count(list1, c)
print(count.__doc__)
print(a)