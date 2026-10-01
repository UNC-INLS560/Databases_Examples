import sqlite3

def display_beverage(drink):

    print(f"{drink[2]}: {drink[3]}")
    print(f"   Calories: {drink[4]}")
    print(f"   Total Fat (g): {drink[5]}")
    print(f"   Sugars (g): {drink[12]}")
    print(f"   Caffeine (mg): {drink[18]}")
    print()

def main():
    # Open a SQLlite connection to starbucks_drinkMenu.db.
    connection = sqlite3.connect("starbucks.db")
    cursor = connection.cursor()

    # Search by drink name until the user decides not to search any more.
    search_term = input("Enter a drink name to search for (or press Enter to quit): ")
    while search_term != "":
        if search_term != "":
            # Tokenize the search term.
            search_keywords = search_term.split()
            # Build a SQL query that searches for the keywords in the drink name and drink preparation.
            query = "SELECT * FROM starbucks_drinkMenu WHERE "
            query += " AND ".join([f"(drink_name LIKE '%{keyword}%' OR drink_prep LIKE '%{keyword}%')" for keyword in search_keywords])
            cursor.execute(query)
            # When we fetch results, we get a LIST of TUPLES, where each tuple is a row in the result set.
            drinks = cursor.fetchall()
            if len(drinks) == 0:
                print(f"No drinks found matching '{search_term}'.")
            else:
                print(f"Found {len(drinks)} drinks matching '{search_term}':")
                for drink in drinks:
                    display_beverage(drink)
        print()
        print()
        print("-------------------------------")
        search_term = input("Enter a drink name to search for (or press Enter to quit): ")
        print()

    # Close the connection.
    connection.close()

main()