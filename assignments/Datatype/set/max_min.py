# program to find maximum and minimum in set 

def min_set(min_1):
    return max(min_1)

min_1 = (1, 5, 4, 6, 7, 10, 25)
b = min_set(min_1)
print(f'The max number is: {b}')


def max_set(max_1):
    return min(max_1)

max_1 = {1, 4, 7, 8, 6, 3, 2}
a = max_set(max_1)
print(f'The min number is: {a}')