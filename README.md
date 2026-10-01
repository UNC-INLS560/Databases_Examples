# Exercises to Demonstrate Database Access from Python

This repository shows two set of examples for creating and querying a database with Python.

Both examples uses SQLite which is a file-based database that doesn't need any type of server software. The databases are stored as .db files (see patients.db and starbucks.db). There are two files for creating databases (one for each dataset) and two files for querying the databases (one for each dataset).

Note that SQL is not a formal learning objective for this course! If you are interested in databases, classes such as INLS 523 or CHIP 732 could be good options for learning more. In this class, we just demonstate what is possible without formally teaching anything about SQL or relational databases.

## Data

There are two datasets included in this repository.

1. Basic medical data for a cohort of 1000 patients, generated synthetically using Claude AI tools. No real patient data is included in this example, and no real data was used to derive the inlucded dataset.  The incluced dataset is 100% artificial.  The actual data can be found in synthetic_patients.csv. 

2. Starbucks drink nutrition information, obtained from Kaggle via the following URL. Note that this page was created in 2017 and very likely does not reflect the current menu options nor up-to-date nutriion data. The actual data can be found in starbucks_drinkMenu_expanded.csv.
https://www.kaggle.com/datasets/starbucks/starbucks-menu

## Database Creation

The two Python creation scripts (create_patient_db.py and create_starbucks_db.py) both
begin by parsing the input CSV files. The result is a "list of lists"
representing the full data table included in the CSV  files. An additional list
containing the names of columns is also created.

After the data is loaded, the Python scripts connect to the database, drop any old tables, and create new tables with a schemas found in the CSV data files.  Once the database tables are created, the scripts insert the rows of data found in the list of lists.

## Database Querying

The two Python query scripts (query_patients.py and query_starbucks.py) both connect to their corresponding SQLite database and make queries against the available tables.

For the patient database, the program query's for data about age and weight for three distinct cohorts: (a) all patients, (b) patients with diabetes, and (c) patients with medicare. Average age and weight information is then calculated for each of these three subsets to allow comparisons. This allows us to check, for example, if the average age of medicare patients is older (expected!) or younger compared to the overall population.

For the Starbucks database, the program allows users to type in a partial product name (e.g., Latte). That partial product name is then used as a constraint against the database to query for all matching products. A few attributes for the resulting products that match the search are displayed on the console. This demonstrates how user input can control the query performed against the database.