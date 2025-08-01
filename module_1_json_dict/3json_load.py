import json

# Read JSON file into dict
with open("input/sample.json", "r") as f:
    data = json.load(f)

print(type(data))

print("Name from file:", data.get("name"))

# Modify and save back
data["age"] = 40

with open("output/updated_sample.json", "w") as f:
    json.dump(data, f, indent=2)

print("File saved to output/updated_sample.json")


"""
JSON Module Usage Summary:

1. json.load(file)
   - Reads JSON data from a file object and returns a Python object.

2. json.loads(json_string)
   - Parses a JSON-formatted string and returns a Python object.

3. json.dump(obj, file)
   - Writes a Python object as JSON to a file object.

4. json.dumps(obj)
   - Converts a Python object to a JSON-formatted string.

Use `load`/`dump` when working with files.
Use `loads`/`dumps` when working with JSON strings.
"""
