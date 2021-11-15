# Write a script to print both the area and the circumference of the rectangle. use variables like width, height, area,circum. ask input from the user
width = int(input('enter a width of rectangle: '))
height = int(input('enter a height of rectangle: '))
area = width * height 
circum = 2 * (width + height)
print(f'the area of rectangle is ', area)
print(f'the circumference of rectangle is ', circum)


# Write a script that has a variable holding the radius of a circle and prints out the area of the circle and the circumference of the circle. use variables : r, pi, area, circum ,ask input from the user
# radius, area, circumference of circle, 
print('\n')
circum = int(input('enter a circumference of circle: '))
pi = float(input('enter a value of pie: '))
r = int(input('enter a radius of circle: '))
circle_radius = circum / 2 * pi
area = pi * r * r
circum = 2 * pi * r
print(f'the radius of circle is ', circle_radius)
print(f'the area of circle is ', area)
print(f'the circumference of circle is ', circum)


# Write a script that has two numbers a and b and prints out the results of a+b, a-b, a*b, a/b, ask input from the user
print('\n')
a = int(input('enter a value of a: '))
b = int(input('enter a value of b: '))
sum = a + b
sub = a - b
mult = a * b
div = a/b
print(f'sum of a and b is ', sum)
print(f'subtracting a from b and result is ', sub)
print(f'multiplication between a and b is ', mult)
print(f'dividing a from b is ', div)


# Take the sentence:  Store each word in a separate variable, then print out the sentence on one line using print,
print('\n')
line1 = input('Enter first word: ')
line2 = input('Enter next word: ')
line3 = input('Enter next word: ')
line4 = input('Enter next word: ')
print(f"{line1}{line2}{line3}{line4}")


# Write a program that will convert degrees celsius to degrees fahrenheit.,
print('\n')
deg_cel = int(input('Enter your temperature in celcius: '))
def_frn = (deg_cel * 9 / 5) + 32
print(f'your body temperature is ',def_frn)

# Write a Python program to print the following string in a specific format (see the output). "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"  
print('\n')
print("use this poem: Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are")
a = input('Enter a first line of poem: ')
b = input('Enter a next of poem: ')
c = input('Enter a next of poem: ')
d = input('Enter a next of poem: ')
e = input('Enter a next of poem: ')
f = input('Enter a next of poem: ')
print(f"{a}\n {b}\n   {c}\n{d}\n {e}\n   {f}\n")
