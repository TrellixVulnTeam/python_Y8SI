# copy of data 

f1 = open('file.txt', mode = 'r')
f2 = open('file3.txt', mode = 'w')
data = f1.read()
f2.write(data)
f1.close()
f2.close()


# error 
# with statement 
with open('file.txt') as f:
    data = f.read()
    print(data)
    print(f.closed)
print(f.close)