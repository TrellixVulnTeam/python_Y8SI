# Program to swap two elements in a list

def swaping(sw1, pos1, pos2):
    '''Program to swap two elements in a list'''
    sw1[pos1], sw1[pos2] = sw1[pos2], sw1[pos1]
    # index 1 value = 2 is swap with index 4 value = 5
    # pos1 = index 1 
    # pos2 = index 4 
    return sw1

# we have index from 0 to 4
sw1=[1, 2, 3, 4, 5]
# here pos refers a positiona nd numbers refers tha index of list
pos1, pos2 = 1 , 4
a = swaping(sw1, pos1, pos2)
print(a)

