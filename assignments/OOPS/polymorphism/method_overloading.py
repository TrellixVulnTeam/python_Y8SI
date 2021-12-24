# mothod overloading 
# parent class 
class programming:

    # property
    DataStructure = True
    Algorithms = True 

    # function practical 
    def practical(self):
        print("perfect practice makes man perfect")

    # function consistency 
    def consistency(self):
        print('hard work along with consistancey makes man good')

# child class 
class python(programming):
    # function 
    def consistency(self):
        print('Hard work along with consistencey can defit a talent')

py = python()
py.consistency()
py.practical()