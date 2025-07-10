import json

# JSON string (as you'd get from API)
json_string = '{"name": "John Doe", "age": 35, "gender": "male"}'

# Convert JSON string → Python dict
person_dict = json.loads(json_string)
print("Python dict:", person_dict)

# Access fields
print("Name:", person_dict["name"])

# Convert Python dict → JSON string
new_json = json.dumps(person_dict)
print("Back to JSON:", new_json)

# pretty print to console

print(json.dumps(person_dict, indent=2))
