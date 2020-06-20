import json
f = open('milk.json',)
data = json.load(f)

for i in data['emp_details']:

    print(i)

f.close()