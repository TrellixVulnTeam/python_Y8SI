# python program to sum of all items in dictionary 

def sum_dict(d):
    sum  = 0
    for i in d.values():
        sum = sum + i
    print(f'sum of the dictionary is: {sum}')

d = {1: 10, 2: 20, 3:30}
sum_dict(d)