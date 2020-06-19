import json
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
json_object = json.dumps(dictionary, indent=4)

with open("milk.json", "w") as outfile:
    outfile.write(json_object)