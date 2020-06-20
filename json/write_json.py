import json
dictionary = {"emp_details": [
      {
        "emp_name": "Shubham",
        "email": "ksingh.shubh@gmail.com",
        "job_profile": "intern"
      }]}
json_object = json.dumps(dictionary, indent=4)

with open("milk.json", "w") as outfile:
    outfile.write(json_object)