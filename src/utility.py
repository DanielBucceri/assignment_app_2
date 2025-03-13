import json
from tabulate import tabulate
import pandas as pd

PROFILE_FILE = "data/profile.json" # File storing player profiles and scores
LEADERBOARD_FILE = "data/Leaderboard.json" # File storing the sorted leaderboard data

def choose_from_menu():
    """
    Displays a menu of key-value pairs and prompts the user
    to choose an option by entering the corresponding number.
    
    Returns:
        tuple:" a tuple containing the selected category name and the corresponding number.
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
        32: "Entertainment: Cartoon & Animations",
    }

    # Display the menu
    print("Please choose question category:")
    for key, value in categories.items():
        print(f"{key}: {value}")

    # Prompt the user to enter a number
    while True:
        try:
            choice = int(
                input("Enter the number corresponding to your category choice: ")
            )
            if choice in categories:
                return categories[choice], choice
            else:
                print("Invalid choice. Please choose a valid number from the menu.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def display_leaderboard():
    """
    loads data from profile.json, sorts it by high_score in descending order,
    writes the sorted data to Leaderboard.json, and displays the leaderboard in the terminal using tabulate.
    
    Retruns: List of the sorted leaderboard data or none if errror occurs.
    """
    try:
        # Step 1: Load data from profile.json
        with open(PROFILE_FILE, "r") as file:
            data = json.load(file)

        leaderboard = [
            {"username": user["username"], "high_score": user["high_score"]}
            # for each item in data (json file). 
            # adds to leaderboard list item.[keyValue]
            for user in data
        ]
        #  Sort by high_score in descending order
        sorted_leaderboard = sorted(
            leaderboard, key=lambda x: x["high_score"], reverse=True
        )

        #  Write sorted leaderboard to leaderboard.json
        with open(LEADERBOARD_FILE, "w") as file:
            json.dump(sorted_leaderboard, file, indent=4)

        #  Display leaderboard to terminal using pandas and tabulate
        df = pd.DataFrame(sorted_leaderboard)
        print(tabulate(df, headers="keys", tablefmt="grid"))

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: The profile file contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def read_json(file):
    """
    Reads data from a JSON file.
    
    args:
        file: str: The path to the JSON file.   
    
    Returns:
        dict: The data loaded from the JSON file.
    
    raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON file. 
    """
    try:
        # Open and load the JSON file
        with open(file, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return print(f"Error: File '{PROFILE_FILE}' not found.")
    except json.JSONDecodeError:
        return print(f"Error: File '{PROFILE_FILE}' is not a valid JSON file.")


def save_json(file_path, data):
    """
    Saves data to a JSON file.
    
    args: file_path: str: The path to the JSON file.
        data: dict: The data to save to the file.
        
    raises:
        Exception: If an error occurs while saving the data.    
    """
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Could not save data to '{file_path}' ({e})")
