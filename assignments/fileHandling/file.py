# write mode 
f = open('file.txt', mode = 'w')
f.write('hello this is python text file which is open and write')
f.close()
print('file written successfully')

# text mode: the date inside txt. file it treate as a string or str type 

# binary mode:  
print()
f = open('file.txt', 'rb') # read binary data 
data = f.read()
print(data)
f.close()

# read mode 
f = open('file.txt', mode = 'r')
data = f.read()
print()
print('Reading the file: ')
print(data)
print(type(data))
f.close()


# file object  variables 
# f = open('file.txt', mode = 'r', encoding= 'utf-8') # binary data doesnot take encoding value 
f = open('file.txt', mode = 'rb+') 
print('File name: ', f.name)
print('File mode: ', f.mode)
print('type: ', type(f))
print('File redable: ', f.readable())
print('File writable: ', f.writable())
# print('File close: ', f.closed())
f.close()
# print('File closed: ',f.closed())



# checking file exist or not 
print()
import os
r = os.path.isfile('file.txt')
print(r)

if os.path.isfile('file.txt'):
    f = open('file.txt')
    print('file Opened')
    f.close()
else:
    print('file not found')
    print()