import json
# newline delimeted json


def read_ndjson(file_path):
    with open(file_path) as f:
        for line in f:
            print(type(line))
            resource = json.loads(line)
            if resource['resourceType'] == 'Patient':
                name = resource.get('name', [{}])[0]
                given = name.get('given', [''])[0]
                family = name.get('family', '')
                print(
                    f"Patient: {given} {family}, Gender: {resource.get('gender')}")


if __name__ == "__main__":
    read_ndjson('input/patients.ndjson')
