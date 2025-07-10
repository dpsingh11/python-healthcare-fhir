import json

# Read JSON file into dict
with open("input/sample.json", "r") as f:
    data = json.load(f)

print("Name from file:", data.get("name"))

# Modify and save back
data["age"] = 40

with open("output/updated_sample.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ File saved to output/updated_sample.json")
