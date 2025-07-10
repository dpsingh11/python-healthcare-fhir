import csv


def read_patient_csv(file_path):
    with open(file_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Patient ID: {row['id']}")
            print(f"Name     : {row['name']}")
            print(f"Gender   : {row['gender']}")
            print(f"DOB      : {row['birthDate']}")
            print("-" * 30)


if __name__ == "__main__":
    read_patient_csv('input/patients.csv')
