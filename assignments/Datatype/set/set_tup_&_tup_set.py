# python program to convert set in tuple and tuple into set

def set_tuple(a):
    '''the function will convert set in to tuple'''
    print(a)
    print(type(a))

    # typecasting to tuple 
    print()
    a = tuple(a)
    print(a)
    print(type(a))

a = {'set', 'converstion', 1, 4,5}
set_tuple(a)

print()
def tuple_set(b):
    '''the function will convert tuple to set'''
    print(b)
    print(type(b))
     
    # type casting to set
    print()
    b = set(b)
    print(b)
    print(type(b)) 

b = 1, 2, 3, 4, 5
tuple_set(b)