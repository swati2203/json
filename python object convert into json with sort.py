import json
from pickle import TRUE


dic={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}
file=json.dumps(dic,indent=2,sort_keys=True)
print(file)