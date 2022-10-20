import json, csv

#JSON String
employee = '{"id": "09", "name": "Nitin", "department":"Finance"}'

# convert string to python dict
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print("/n")

# Convert Python dict to JSON
json_object = json.dumps(employee_dict, indent=4)
print(json_object)
print(type(json_object))

# CSV Exporter
# fname, sname, description, can-bowl
data = [
["jos", "buttler", "opening batsman",False],
["alex", "hales", "opening batsman",False],
["dawid", "malan", "top order batsman",False],
["ben", "stokes", "all-rounder",True],
["jonny", "bairstow", "power hitter",False],
["moeen", "ali", "experienced all-rounder",True],
["chris", "woakes", "all-rounder",True],
["david", "willey", "fast bowler",True],
["chris", "wood", "fast bowler",True],
["adil", "rashid", "spin bowler",True],
["reece", "topley", "fast bowler",True]
]
y = 'team.csv'
with open(y, 'w') as work:
    z = csv.writer(work)
    z.writerows(data)