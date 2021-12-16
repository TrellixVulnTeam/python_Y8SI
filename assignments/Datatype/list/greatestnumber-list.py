# python program to finf the greatest number in list 
def greatestNumber(a):
    '''the pprogram is design to find the greatest numbet from the list '''
    a.sort()
    return a[-1]

b =greatestNumber(a=[10, 1, 2, 5, 15, 20, 30, 50, 60])
print(greatestNumber.__doc__)
print(b)
