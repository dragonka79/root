import json

# Loading from a string explicitly given

jsonstr = """{"people" : [{"firstName": "Joe","lastName": "Jackson","gender": "male","age": 28,"number": "7349282382","Active": true},
{"Name": {"FN": "James", "LN": "Smith"},"gender": "male","age": 32,"number": "5678568567","Active": false}]}"""

jsonobj = json.loads(jsonstr)

print('\b')
print('The json object is:\n', jsonobj)
print("Type of the object: ", type(jsonobj))
print("Type of 'people': ",type(jsonobj['people']))
print("The second item in 'people': ",(jsonobj['people'][1]))

# Loading from a json file

jsonobj = json.load(open('sample4.json'))

print('\b')
print('The json file is:\n', jsonobj)

print("Type of the object: ", type(jsonobj))
print("Type of 'people': ",type(jsonobj['people']))
print("The second item in 'people': ",(jsonobj['people'][1]))