# nested dictionary
# person is dict which has two keys
# first key is name --- which has dict as value
# second key is contacts --- which has list of dict

person = {
    "name": {
        "first": "John",
        "last": "Doe"
    },
    "contacts": [
        {"type": "email", "value": "john@example.com"},
        {"type": "phone", "value": "+91-1234567890"}
    ]
}

# Access nested dict
print("First name:", person["name"]["first"])
print("Last name:", person["name"]["last"])

# Loop through list of contacts
for contact in person["contacts"]:
    print(f"{contact['type']}: {contact['value']}")
