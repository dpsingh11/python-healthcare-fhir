import json


def read_fhir_bundle(file_path):
    with open(file_path) as f:
        data = json.load(f)

    print("Reading FHIR Bundle...\n")
    # get() to fall safe provide default value
    for entry in data.get('entry', []):
        resource = entry.get('resource', {})
        if resource.get('resourceType') == 'Patient':
            name = resource.get('name', [{}])[0]
            given = name.get('given', [''])[0]
            family = name.get('family', '')
            print(f"Patient Name : {given} {family}")
            print(f"Gender       : {resource.get('gender')}")
            print(f"Birth Date   : {resource.get('birthDate')}")
            print("-" * 30)


if __name__ == "__main__":
    read_fhir_bundle('input/fhir_bundle.json')
