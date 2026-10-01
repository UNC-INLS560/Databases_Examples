import sqlite3

def query_and_display_avg_age_and_weight(query, cursor):
    cursor.execute(query)
    # When we fetch results, we get a LIST of TUPLES, where each tuple is a row in the result set.
    patients = cursor.fetchall()

    # Get overall ages and weights as individual lists. Because we selected for "age, weight_lbs", the 
    # 0th element is age and the 1st element is weight for each patient matching the query.
    ages = [patient[0] for patient in patients]
    weights = [patient[1] for patient in patients]

    # Calculate and display the averages.
    print(f"Average age: {sum(ages) / len(ages):.2f} years.")
    print(f"Average weight: {sum(weights) / len(weights):.2f} lbs.")


def main():
    # Open a SQLlite connection to patients.db.
    connection = sqlite3.connect("patients.db")
    cursor = connection.cursor()

    # Query the database for all patients and display height and weight information.
    print("STATISTICS FOR ALL PATIENTS:")
    query_and_display_avg_age_and_weight("SELECT age, weight_lbs, height FROM patients", cursor)
    print()

    # Now query the database for patients with a diabetes diagnosis.
    print("STATISTICS FOR DIABETES PATIENTS (are they heavier?):")
    query_and_display_avg_age_and_weight("SELECT age, weight_lbs FROM patients WHERE problem_list LIKE '%diabetes%'", cursor)
    print()
    
    # Finally, query the database for patients with medicare.
    print("STATISTICS FOR MEDICARE PATIENTS (are they older?):")
    query_and_display_avg_age_and_weight("SELECT age, weight_lbs FROM patients WHERE insurance_type = 'Medicare'", cursor)
    print()

    # Close the connection.
    connection.close()

main()