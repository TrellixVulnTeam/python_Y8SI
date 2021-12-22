# python grogram to demostrate 
# multiple inheritance 

# Base class 1
class Mother:
    motherName = ''
    def mother(self):
        print(self.motherName)


# Base class 2
class Father:
    fatherName = ''
    def father(self):
        print(self.fatherName)


# Derive class 
class child(Mother, Father):

    # display the name here 
    def parents(self):
        print('Father : ', self.fatherName)
        print('Mother : ', self.motherName)

# 
s1 = child()
s1.fatherName = 'Father'
s1.motherName = 'Mother'
s1.parents()