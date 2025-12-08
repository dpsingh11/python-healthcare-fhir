import json

def ndjson_to_bundle(ndjson_path, bundle_path):
    entries = []

    with open(ndjson_path) as f:
        for line in f:
            resource = json.loads(line)
            entries.append({
                "resource": resource
            })

    bundle = {
        "resourceType": "Bundle",
        "type": "collection",
        "entry": entries
    }

    with open(bundle_path, 'w') as f:
        json.dump(bundle, f, indent=2)

    print(f"Bundle written to {bundle_path}")


if __name__ == "__main__":
    ndjson_to_bundle('input/patients.ndjson', 'output/patient_bundle.json')
