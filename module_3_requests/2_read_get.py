import requests

fhir_base_url = 'https://server.fire.ly/Patient'
headers = {"Content-Type": "application/fhir+json"}

patient_id = "a300358f-5942-4da2-aca0-9fefed48c4e5"  # Replace with your ID
response = requests.get(f"{fhir_base_url}/{patient_id}")

print(type(response))

print(response)

print("Status:", response.status_code)
if response.status_code == 200:
    print(f"Patinet with resource id : {patient_id} found \n")
    print("Patient Resource:", response.json())
else:
    print(f"Patient with id :{patient_id} not found on the server")
