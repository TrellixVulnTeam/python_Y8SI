# read and write file 
from os import write

# f = open('file2.txt', mode = 'w')
# f.write('begining of file')
# f.close()
# print('success')
# print()

f = open('file2.txt', mode= 'r+') # read and write method 
print(f.tell())
data = f.read()
print(f.tell())
f.write('thsi is r+ method means first read and write the file')
print(f.tell())
print(data)
print(f.tell())


# write then read, it will overwrite existing data 
print()
f = open('file2.txt', mode='w+')
print(f.tell())
f.write('this is new data ')
print(f.tell())

# f.seek()
# print(f.tell())
data = f.read()
print(f.tell())
print(data)
print(f.tell())


# append then read, it wnt overwritr existing data 
f = open('file2.txt', mode='a+')
print(f.tell())
f.write('updated data')
print(f.tell())
data = f.read()
print(f.tell())
print(data)
print(f.tell())
