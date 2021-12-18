# python program to convert set in to string 
def set_to_str(a):
    print(type(a))
    print(a)

    # converting to string 
    a = str(a)
    print(type(a))
    print(a)

a = {'a', 'b', 'c', 'd', 'd', 'e', 'f', 'g', 'h'}
set_to_str(a)