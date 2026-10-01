import csv
import sqlite3

# Constants defining the name of the CSV file and the name of the database.
CSV_PATH = "synthetic_patients.csv"
DB_PATH = "patients.db"


# Load the synthetic patient data CSV file. Return as a header row and a list of data rows.
def load_csv(csv_path):
    csv_file = open(csv_path, newline="", encoding="utf-8")
    reader = csv.reader(csv_file)

    # Get a list of list with the read data.
    data = list(reader)

    # Return the first row as the header and the rest of the rows as data.
    return data[0], data[1:]


# Create a table in the SQLdatabase.
def create_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS patients")
    cursor.execute(
        """
        CREATE TABLE patients (
            patient_id TEXT PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            date_of_birth TEXT,
            age INTEGER,
            sex TEXT,
            blood_pressure TEXT,
            height TEXT,
            weight_lbs INTEGER,
            problem_list TEXT,
            date_of_last_visit TEXT,
            doctor TEXT,
            medication_list TEXT,
            smoking_status TEXT,
            insurance_type TEXT,
            allergy_list TEXT
        )
        """
    )

# Insert rows into the SQL database
def insert_rows(cursor, rows):
    cursor.executemany(
        "INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        rows,
    )


def main():
    # Get the data
    header, rows = load_csv(CSV_PATH)

    # Create a connection to the database, create the table, then insert the data.
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    create_table(cursor)
    insert_rows(cursor, rows)

    # Commit the changes and close the connection to the database.
    connection.commit()
    connection.close()

    print(f"Inserted {len(rows)} rows into '{DB_PATH}'.")


main()
