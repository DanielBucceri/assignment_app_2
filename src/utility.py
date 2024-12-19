import json
from tabulate import tabulate   
import pandas as pd
PROFILE_FILE = "data/profile.json"
LEADERBOARD_FILE = "data/Leaderboard.json"

def choose_from_menu():
    """
    Displays a menu of key-value pairs and prompts the user to choose an option by entering the corresponding number.
    
    Returns:
        tuple: The chosen number and corresponding catgeory .
    """
    # Define the key-value pairs
    categories = {
    9: "General Knowledge",
    10: "Entertainment: Books",
    11: "Entertainment: Film",
    12: "Entertainment: Music",
    13: "Entertainment: Musicals & Theatres",
    14: "Entertainment: Television",
    15: "Entertainment: Video Games",
    16: "Entertainment: Board Games",
    17: "Science & Nature",
    18: "Science: Computers",
    19: "Science: Mathematics",
    20: "Mythology",
    21: "Sports",
    22: "Geography",
    23: "History",
    24: "Politics",
    25: "Art",
    26: "Celebrities",
    27: "Animals",
    28: "Vehicles",
    29: "Entertainment: Comics",
    30: "Science: Gadgets",
    31: "Entertainment: Japanese Anime & Manga",
    32: "Entertainment: Cartoon & Animations"
}


    # Display the menu
    print("Please choose question category:")
    for key, value in categories.items():
        print(f"{key}: {value}")

    # Prompt the user to enter a number
    while True:
        try:
            choice = int(input("Enter the number corresponding to your category choice: "))
            if choice in categories:
                return categories[choice], choice
            else:
                print("Invalid choice. Please choose a valid number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_leaderboard_as_table():

    try:
        # Read the JSON file
        with open(LEADERBOARD_FILE, 'r') as file:
            data = json.load(file)

        # Check if data is a list of dictionaries
        if not isinstance(data, list):
            
            return print("Invalid Json.")

        # Create a DataFrame from the data
        df = pd.DataFrame(data)

        # Use tabulate to print the DataFrame as a table
        print(tabulate(df, headers='keys', tablefmt='grid'))
        input("Press enter to continue...")

    except FileNotFoundError:
        print(f"Error: File '{LEADERBOARD_FILE}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{LEADERBOARD_FILE}' is not valid Json .")
