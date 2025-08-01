import json

REQUIRED_FIELDS = ['name', 'gender', 'birthDate']


def validate_patients(file_path):
    with open(file_path) as f:
        bundle = json.load(f)

    for entry in bundle.get('entry', []):
        resource = entry.get('resource', {})
        if resource.get('resourceType') == 'Patient':
            print(f"Validating Patient ID: {resource.get('id')}")
            for field in REQUIRED_FIELDS:
                if field not in resource:
                    print(f"  Missing field: {field}")
                else:
                    print(f"   {field} found")
            print("-" * 30)


if __name__ == "__main__":
    validate_patients('input/fhir_bundle.json')
