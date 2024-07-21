import sys
import json
from jsonpath_ng.ext import parse

if __name__ == "__main__":
    if len(sys.argv) >4 or  len(sys.argv) <4:
        print("Введите 3 аргумента")
    else:
        valuesPath = sys.argv[1]
        testsPath = sys.argv[2]
        reportPath = sys.argv[3]

with open(valuesPath) as f: ids = json.load(f)
with open(testsPath) as f: vals = json.load(f)

bnew = {}

for i in ids['values']:
    bnew[str(i['id'])] = i['value']

def find(collection, key):
    if isinstance(collection, dict):
        if key in collection:
            yield collection
        for val in collection.values():
            yield from find(val, key)
    elif isinstance(collection, list):
        for val in collection:
            yield from find(val, key)

for collection in find(vals, 'id'):
    if isinstance(collection['id'], str):
        try:
            collection['value'] = str(bnew[collection['id']])
        except:
            print(end='')
    else:
        try:
            collection['value'] = str(bnew[str(collection['id'])])
        except:
            print(end='')
    
with open('report.json', 'w') as f: 
    json.dump(vals, f, indent=4)