import requests
import json
"""
pip - Python Package Installer:

- `pip` is the standard package manager for Python.
- It allows you to install and manage additional libraries and dependencies that are not part of 
the Python standard library.

Common pip commands:
1. Install a package:
   pip install <package_name>

2. Install specific version:
   pip install <package_name>==1.2.3

3. Upgrade a package:
   pip install --upgrade <package_name>

4. List installed packages:
   pip list

5. Save dependencies to requirements.txt:
   pip freeze > requirements.txt

6. Install from requirements.txt:
   pip install -r requirements.txt

Useful for installing packages like `requests`, `fhir.resources`, `pandas`, `matplotlib`, etc.
"""

'''
1. create virtual environment 
    python -m venv venv
2. activate the virutal env 
    .\venv\Scripts\activate

    once its activated you will see somthing like (venv)-- which tells you are in virtual env now

3. crate a file at root location as requirements.txt under that we can have module names which we want 
    to install like 
    requests
    fhir.resources

4. pip install -r requirements.txt  (this will install all the modules in one go to the virtual env)

5. you can install individually using the command pip install <packagename> also

6. use command pip list in your terminal and see if you have required packages there 

you are good to go now 
'''

patient_resource = {
    "resourceType": "Patient",
    "name": [{
        "use": "official",
        "family": "Uthapa",
        "given": ["Robin"]
    }],
    "gender": "male",
    "birthDate": "1999-07-29"
}

# you can see currently this is deserialized python dict object which can not travel over the api request
print(f"before serialization, {type(patient_resource)}")

# what we gona do is making it serialized so that it can go over the internet to other system
patient_data = json.dumps(patient_resource)

print(f"after serialization type is : {type(patient_data)}")

# fhir base url to publicly available firely server

fhir_base_url = 'https://server.fire.ly/Patient'

headers = {"Content-Type": "application/fhir+json"}

'''
these configuration details are repeating accross the projects 
vilating on the software engineering Principals
we absolutely should move repeated values like fhir_base_url and headers 
to a common config or utility module to follow good coding practices like DRY (Don't Repeat Yourself).
'''

# post for creating a new resource
response = requests.post(fhir_base_url, headers=headers,
                         data=patient_data)

print(type(response))

# status code 201 -- created
print("Status:", response.status_code)

# see the response to see in console we have to make it deserilize
if response.status_code == 201:
   print("Response:", response.json())

res = response.json()
print(type(res))

patient_res_id = res.get("id")

print(f"Patient resource created with id : {patient_res_id}")
