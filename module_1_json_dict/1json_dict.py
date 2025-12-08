import json
# JSON string (as you'd get from API)
# data type === type of data + supported operations  not just data type 
# IT evoluction is nothing but "Abstraction" - Design Thinking, Architecture First approach 
json_string = '{"name": "John Doe", "age": 35, "gender": "male"}'

# Convert JSON string → Python dict (deserialize)
person_dict = json.loads(json_string)
print("type after conversion ", type(person_dict))
print("Python dict:", person_dict)

#now we can acees dict related methods
# person_dict.get()
# Access fields
print("Name:", person_dict["name"])

# Convert Python dict → JSON string (serialization)
new_json = json.dumps(person_dict)
print(type(new_json))
# new_json.replace
print("Back to JSON string:", new_json)

# pretty print to console
print(json.dumps(person_dict, indent=6))




"""
1. Serialization
Converting an in-memory Python object (like a dict, list, or class instance) into a format that can be
 stored or transmitted 
(like JSON or a file).

Example in Python: Using json.dumps() or json.dump().

You serialize when you need to:
    1. Send data over a network (e.g., POST to FHIR server)
    2. Store data in a file or database

2. Deserialization
Converting serialized data (JSON string or file) back into a Python object (dict, list, or class).

Example in Python: Using json.loads() or json.load().

You deserialize when you need to:
    1. Process API response (FHIR server returns JSON → you convert to dict)
    2. Load stored files into memory for manipulation
"""
