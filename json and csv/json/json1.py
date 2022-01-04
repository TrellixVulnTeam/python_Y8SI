import json 

# json.lodas() => it is use to convert the JSON string to python dictionary 
# convert from python to json
# data = '{"var1":"YOGESH", "Var2":"name" }'
# value = json.loads(data) # convert json string to py dictionaty
# print(f'conver from python to JSON: {value}')
# print(value['var1']) #gives the value which is at var1
# print()

# # json.load() => it is use to read the JSION documents file from JSON 
# # convert from JSON to python 
# x = '{"name" : "hello", "age": 19, "class": 12}'
# y = json.load(x)
# print(f"convert from json to python: {y}")
# print()

# json.dump()
# convert python objects into JSON and print the value 
data2 = {
    "name" : "yogesh", 
    'cars' : ['BMW', 'farari', 'Tesla', 'volvox'],
    'frns' : ['umesh', 'shahisnuta'], 
    'isgood' : True # json make it like js with the help of .dumps and we can use this data into js too
}
value2 = json.dumps(data2)
print(value2)
# print(value2['isgood'])


# sort_keys_parametses: use to specify if the result should be sorted or not 
# sort the data in alphabatical order
hello = {
    "name " : 'python json', 
    'age' : 19, 
    'sigle' : True, 
    'pet' : ['cat', 'dog'], 
    'drive' : False, 
    'languages' : ['python', 'js', 'react_framework', 'html', 'css']
}
a = json.dumps(hello, sort_keys=True)
b = json.dumps(hello, indent=4) # not clear
print(a)
print(b)

# seperator 
# code are call from above 
# trow an error, keyword arguments 
# z = json.dumps(hello, indent=4, seperarots=(".", "="))

