import json

with open('data.json', 'r') as myfile:
    data = myfile.read()
    obj = json.loads(data)
    print(obj)