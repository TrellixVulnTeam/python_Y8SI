# 1. Write a script that has two numbers a and b and prints out the results of a+b, a-b, a*b, a/b
# variables 
a = 43
b = 23

add =  a + b
print(f"the addition of a and b is ", add)

sub = a - b
print(f"the subtracted value of b from a is ", sub)

mult = a * b
print(f"the multiplication between a and b is ", mult)

div = a / b
print(f"the value after dividing a by b is ", mult)


# 2. Write a script that has a variable holding the radius of a circle and prints out the area of the circle and the circumference of the circle.


# radius of a circle
print("\n")
print('radius of a circle')
print("Enter a circumfrence of circle: ")
C = int(input()) 
print("Enter a value of pie (use : 3.1415): ")
pie = float(input())
radius = C / 2 * pie
print(f"Radius of circle is ", radius)

# area of circle 
print("\n") 
print('area of circle')
print("Enter a value of pie (use: 3.1415): ")
Pie = float(input())
print("Enter a radious of circle: ")
rd = int(input())
area =  Pie*rd*rd
print(f"The area of circle is ", area)

# circumference of the circle.
print("\n") 
print(' circumference of the circle.')
print("Enter a value of pie (use: 3.1415): ")
Pi = float(input())
print("Enter a radious of circle: ")
radius = int(input())
Cir = 2*Pi*radius
print(f"The Circumference of circle is: ", Cir)

print("\n")
# 3. Write a Python program to print the following string in a specific format (see the output). 
a = "Twinkle, twinkle, little star,\n"
b = "  How I wonder what you are!\n"
c = "    Up above the world so high,\n"
d = "    Like a diamond in the sky.\n"
e = "Twinkle, twinkle, little star,\n"
f = "  How I wonder what you are\n" 
output = a + b + c + d + e + f
print(output)

# Write a program that will convert degrees celsius to degrees fahrenheit.
print("\n")
print("Write a program that will convert degrees celsius to degrees fahrenheit.")
print("Enter a value to convert degrees celsius to degrees fahrenheit: ")
deg_cel = int(input())
deg_frn = (deg_cel * 9 / 5) + 32
print(deg_frn, 'frn')

# Take the sentence:  Store each word in a separate variable, then print out the sentence on one line using print
print("\n")
print("Take the sentence:  Store each word in a separate variable, then print out the sentence on one line using")
sent1 = 'Python is an interpreted high-level general-purpose programming language.'
sent2 = 'Its design philosophy emphasizes code readability with its use of significant indentation.'
sent3 = 'Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.'
sentence = sent1 + sent2 + sent3
print(sentence)

# Write a script to print both the area and the circumference of the rectangle. use variables like width, height, area,circum
print('\n')
width =  input('enter a width of rectangle: ')
height = input('enter a height of rectangle: ')
area = int(width) * int(height)
circum = 2 * (int(width) + int(height))
print('the area of rectangle is ', area)
print('the circumfrence of recatangle is ', circum)