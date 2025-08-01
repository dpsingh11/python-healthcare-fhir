import json


def bundle_to_ndjson(bundle_path, output_path):
    with open(bundle_path) as f:
        bundle = json.load(f)

    with open(output_path, 'w') as f:
        for entry in bundle.get('entry', []):
            resource = entry.get('resource')
            print(type(resource))
            if resource:
                f.write(json.dumps(resource) + '\n')

    print(f"NDJSON written to {output_path}")


if __name__ == "__main__":
    bundle_to_ndjson('output/patient_bundle.json',
                     'output/extracted_patients.ndjson')
