# writing a file 
f = open('fileread.txt', mode='w')
f.write('hello this is yogesh testing file reading ')
f.close()
print('success')
print()

# reading a file 
f = open('fileread.txt', mode = 'r')
data = f.read()
f.close()
print("file read successfully")
print()

f = open('fileread.txt', mode= 'r')
data = f.read()
print(data)
f.close()
print('file read success')
print()

f = open('fileread.txt', mode='r')
data1 = f.read()
print(data1)
data2 = f.read()
print(data2)
f.close()
print('file read success')
print()