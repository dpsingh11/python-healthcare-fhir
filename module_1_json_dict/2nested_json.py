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

# Loop through list of contacts
for contact in person["contacts"]:
    print(f"{contact['type']}: {contact['value']}")
