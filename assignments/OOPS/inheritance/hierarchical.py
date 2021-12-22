# python program to demostrate the 
# hierarchical inheritance 

# Base class 
class Parent:
    
    def func1(self):
        print('This function is in parent class.')

# derive class 1
class child1(Parent):

    def func2(self):
        print('This function is in child 1.')

# derive class 2
class child2(Parent):

    def func3(self):
        print('This function is in chile 2.')

# derive code 
object1 = child1()
object2 = child2()
print('====================>')
object1.func1()
object1.func2()
print()
print('====================>')
object2.func1()
object2.func3()