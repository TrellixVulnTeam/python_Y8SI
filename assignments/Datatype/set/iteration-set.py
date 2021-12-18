#  python program to demostrate the iteration over the set in python 

# iterating over the numbers 
def num(set1):
    for i in set1:
        print(i)

set1 = {1, 4, 5, 6, 7, 8, 9}
num(set1)

# iterating over the string
print()
def ch(set2):
    for i in set2:
        print(i, end=' ')

set2 = set('HelloPythonDevelopers')
ch(set2)