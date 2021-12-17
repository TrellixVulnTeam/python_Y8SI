# python program to test if element inside a tuple is distinct or not?

# creating a tuple 
a = (1, 2, 3, 4, 4)

# printing the original tuple 
print(f'orginal tuple is {str(a)}')

# testing if the tuple is distinct or not 
result = len(set(a)) == len(a) # converting to set because set donsnot allow to repeate the data and again comparing its will check the value of orginal a 
# set doent alllow ro have a repeated value and while checking the values between string len and orginal a len, string will have less value than orginal a, 
# and when string value will be equal to orginal a value, it will show 'True' else 'False' 

# printing the result
print(f'Is tuple distinct?: {result}')

