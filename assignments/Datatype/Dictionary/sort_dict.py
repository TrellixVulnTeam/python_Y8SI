# Program to Sort Python Dictionaries by Key or Value

def sorted_dict(a):
    for i  in sorted(a):
        print(i, end=' ')

a = {10:10, 2:20000, 30: 3000, 4: 100}
sorted_dict(a)