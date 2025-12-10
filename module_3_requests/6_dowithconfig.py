# Add root directory to Python path
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print(__file__)

print(os.path.dirname(__file__))

import requests
from config import FHIR_BASE_URL, HEADERS


url = f"{FHIR_BASE_URL}/Patient/pat-123"
payload = {
    "resourceType": "Patient",
    "id": "pat-123",
    "name": [{"use": "official", "family": "Doe", "given": ["John"]}],
    "gender": "male",
    "birthDate": "1990-01-01"
}

response = requests.put(url, headers=HEADERS, json=payload)
print(response.status_code)
print(response.json())
print("Patient got created with id :", response.json()["id"])


'''
Python tries to find config.py by checking these locations in order:

1. The current script's directory

2. Entries in the PYTHONPATH environment variable (if any)

3. The system-wide site-packages (where pip installs packages)

4. Any custom entries you add to sys.path
'''

