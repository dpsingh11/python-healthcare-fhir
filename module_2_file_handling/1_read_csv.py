# working with csv in python

import csv
import os
# help(csv.DictReader)


def read_patient_csv(file_path):
    with open(file_path, mode='r') as f:
        reader = csv.DictReader(f)
        print(type(reader))
        for row in reader:
            # print(type(row))
            print(f"Patient ID: {row['id']}")
            print(f"Name     : {row['name']}")
            print(f"Gender   : {row['gender']}")
            print(f"DOB      : {row['birthDate']}")
            print("-" * 30)


def write_patient_csv(new_patients, file_path="input/patients.csv"):
    print(f"Adding new patients: {new_patients}")

    file_exists = os.path.isfile(file_path) and os.path.getsize(file_path) > 0

    with open(file_path, "a", newline="") as f:
        fieldnames = ["id", "name", "gender", "birthDate"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:  # Write header only for new/empty file
            writer.writeheader()

        writer.writerows(new_patients)

    print("CSV written successfully!")


if __name__ == "__main__":
    read_patient_csv('input/patients.csv')

    write_patient_csv([{'id': 11, 'name': 'Harry Potter',
                      'gender': 'male', 'birthDate': '1998-04-24'}])

"""
1. csv.DictReader is a helper class in Python’s built-in csv module that reads a CSV file into a 
sequence of dictionaries, where keys are taken from the header row.

{"id":1,"name":"Bruce Wayne"}......

2. csv.reader (list) : sequence of list you need to manually map the headers here 
good when headers dont matter 

3. 'a' mode → Appends new rows (doesn't delete existing ones)
4. Always check if the file exists before writing headers to avoid duplicates
"""
