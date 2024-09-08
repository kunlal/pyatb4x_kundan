# dictionary operation


#load(read json/dict) and dumps(write string as json/dict) for string (s)
#load and dump for file reading/writing content in json

import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

jsonDict = json.loads(person_string)

print(type(jsonDict))

print(jsonDict['name'])
print(jsonDict['numbers'][1])

#adding multiple elemets
jsonDict['element'] = 1,2,3
print(jsonDict)

#adding nested dic

jsonDict['nested'] = {'city':'saharanpur','bank':{"home":"PNB","Blor":"ICIIC"}}
#update dict numbers 1
jsonDict['numbers'][1] = 100

#using update method

print(jsonDict)

#operation on json string

#adding new key and value
jsonDict["class"] = 12
print(jsonDict)

#accesing element using get key

name = jsonDict.get('name')
print(name)

#updating dict using update method

jsonDict.update({'name':"Sumit"})
print(jsonDict)
#or
jsonDict.update(name = "Kavitha")
print(jsonDict)


#get all the keys and values

keys = jsonDict.keys()
print(keys)
values = jsonDict.values()
print(values)

#loop over dict

for i,j in jsonDict.items():
    print("Items: ",i,j)



