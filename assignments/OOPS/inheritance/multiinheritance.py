# python grogram to demostrate 
# multiple inheritance 

# Base class 1
# class Mother:
#     motherName = ''
#     def mother(self):
#         print(self.motherName)


# # Base class 2
# class Father:
#     fatherName = ''
#     def father(self):
#         print(self.fatherName)


# # Derive class 
# class child(Mother, Father):

#     # display the name here 
#     def parents(self):
#         print('Father : ', self.fatherName)
#         print('Mother : ', self.motherName)

# # 
# s1 = child()
# s1.fatherName = 'Father'
# s1.motherName = 'Mother'
# s1.parents()



# multi-inheritance another example 
class school:

    # constructor 
    def __init__(self, name):
        self.name = name
        print(f'What is the name of your school?')


class Admin:
        print('Who will teach u a Computer Programming?')
        # print(f'the name of our Computer programming Tracher is {self.name}')

class fees:

        print('How much fees do you pay to ur collage?')

class student(school, Admin,  fees):

    # claiing constructor from base class 
    def __init__(self, name, fees, Tname):
        self.fees = fees
        self.Tname = Tname
        super().__init__(name)
        print('============>\nAnswers')
        print(f'The name of my school is {self.name}')
        print(f'The {self.fees} i pay to my {self.name}')
        print(f'The name of my computer programming treacher is {self.Tname}')

obj = student('SDB_Schol', '1000', 'Bikky')
