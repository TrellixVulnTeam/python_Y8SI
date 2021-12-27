# write mode 
f = open('file.txt', mode = 'w')
f.write('hello this is python text file which is open and write')
f.close()
print('file written successfully')

# text mode: the date inside txt. file it treate as a string or str type 

# binary mode:  


# read mode 
f = open('file.txt', mode = 'r')
data = f.read()
print()
print('Reading the file: ')
print(data)
print(type(data))
f.close()