# python program to demostrate the 
# hybrid inheritance 

class school:
    def scl1(delf):
        print('You are in School.')

class student1(school):
    def scl2(self):
        print('This is student 1.')

class student2(school):
    def scl2(self):
        print('This is student 2.')

class student3(student1, school):
    def scl3(self):
        print('This is student 3.')

# deriver's code 
object1 = student3()
object1.scl1()
object1.scl2()
