# python program to demostrate the if list have at least one common element 

def common(set1 , set2):
    set1 = set(set1)
    set2 = set(set2)
    if len(set1.intersection(set2)) > 0:
        return True
    return False


set1 = [1, 4, 5, 6, 7, 8]
set2 = [4, 9, 7, 11, 12, 15]
print(common(set1, set2))