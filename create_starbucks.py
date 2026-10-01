import csv
import sqlite3

# Constants defining the name of the CSV file and the name of the database.
CSV_PATH = "starbucks_drinkMenu_expanded.csv"
DB_PATH = "starbucks.db"


# Load the drink menu data into the database. Return as a header row and a list of data rows.
def load_csv(csv_path):
    csv_file = open(csv_path, newline="", encoding="utf-8")
    reader = csv.reader(csv_file)

    # Get a list of list with the read data.
    data = list(reader)

    # Return the first row as the header and the rest of the rows as data.
    return data[0], data[1:]


# Create a table in the SQLdatabase.
def create_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS starbucks_drinkMenu")
    cursor.execute(
        """
        CREATE TABLE starbucks_drinkMenu (
            id TEXT PRIMARY KEY,
            drink_category TEXT,
            drink_name TEXT,
            drink_prep TEXT,
            calories INTEGER,
            total_fat_g REAL,
            trans_fat_g REAL,
            saturated_fat_g REAL,
            sodium_mg INTEGER,
            total_carbohydrates_g REAL,
            cholesterol_mg INTEGER,
            dietary_fiber_g REAL,
            sugars_g REAL,
            protein_g REAL,
            vitamin_a_percent_dv REAL,
            vitamin_c_percent_dv REAL,
            calcium_percent_dv REAL,
            iron_percent_dv REAL,
            caffeine_mg INTEGER
        )
        """
    )

# Insert rows into the SQL database
def insert_rows(cursor, rows):
    cursor.executemany(
        "INSERT INTO starbucks_drinkMenu VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        rows,
    )


def main():
    # Get the data
    header, rows = load_csv(CSV_PATH)

    # Insert a drink ID column into the data rows. The ID is a string of the form "drink_0001", "drink_0002", etc.
    for i, row in enumerate(rows):
        row.insert(0, f"drink_{i+1:04d}")

    # Also add the ID column to the header row.
    header.insert(0, "id")


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
