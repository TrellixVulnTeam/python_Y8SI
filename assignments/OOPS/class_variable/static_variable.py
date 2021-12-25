# class or static variable 
# python program to show the variables with value assign in class declaration ara class variable 
# class for computer science students 
class CSStudents:
    # class variable 
    stream = 'cse'

    # constructor 
    def __init__(self, name, roll):
    # instance variables 
        self.name = name
        self.roll = roll

# objects of CSStudents 
a = CSStudents('student1', 1)
b = CSStudents('student2', 1)

print()
print(a.stream)
print(b.stream)
print(a.name)
print(b.name)
print(a.roll)
print(b.roll)

# class variables can be accessed using class name also 
print()
print(CSStudents.stream) # print cse

# Now if we change stream for just 'a' object it wont change for object 'b'
a.stream = 'ecs'
print()
print(a.stream) # ecs 
print(b.stream) # cse

# trying to change the stream for all instance of the class we can change it irectly from the class 
# example of change the value of class directly from class variable
CSStudents.stream = 'mechanical engineer'
print()
print(a.stream) # its value wont change because we have change the value of a specificallt. 
print(b.stream) 