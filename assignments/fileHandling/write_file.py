# writing a file 
f = open('write.txt', mode = 'w')
f.write('hello ')
f.write('this is python course ')
f.write('we are working on file handeling ')
f.close()

f = open('write.txt', mode = 'a')
f.write(' we are working on writing method ')
f.write('and append method ')
f.close()
print('write successfully')


# writelines()
f = open('filewritelines.txt', mode='w')
l = ['a\n','b\n','c']
f.writelines(l)
f.close()
print('file written success')

f = open('filewritelines.txt', mode='a')
l = ['a\n','b\n','c\n','d']
f.writelines(l)
f.close()
print('file written success')