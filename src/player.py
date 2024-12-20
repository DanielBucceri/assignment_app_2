from datetime import datetime
import json
import pandas as pd
from utility import choose_from_menu

PROFILE_FILE = "data/profile.json"
LEADERBOARD_FILE = "data/Leaderboard.json"

class Player:
    def __init__(self, username, difficulty="medium", high_score=0, category=19, history=[]):
        self.username = username
        self.difficulty = difficulty
        self.category = category
        self.high_score = high_score
        self.history = history
        
    def update_preferences(self, username, difficulty, category):
        self.username = username
        difficulty_input = int(input("Enter corresponding number to select difficulty. 1.easy 2.medium 3.hard: "))
        match difficulty_input:
            case 1: difficulty = "easy"
            case 2: difficulty = "medium"
            case 3: difficulty = "hard"
            case _: difficulty = "medium"  
        category = choose_from_menu()  
        try:
        # Open and load the JSON file
         with open(PROFILE_FILE, "r") as file:
            data = json.load(file)
            # Search for the matching username
            for user in data:
                if user.get("username").lower() == username.lower():
                    # Update only the fields that are provided
                        if difficulty:
                            user["difficulty"] = difficulty
                        if category:
                            user["category"] = category
                        with open(PROFILE_FILE, "w") as file:
                            json.dump(data, file, indent=4)

                print(f"Preferences for'{username}' updated successfully.")
                return True
            else:
                print(f"User '{self.username}' not found.")
                return False
        except FileNotFoundError:
            return print(f"Error: File '{PROFILE_FILE}' not found.")
        except json.JSONDecodeError:
            return print(f"Error: File '{PROFILE_FILE}' is not a valid JSON file.")



    def display_high_score(self):
            """
            Opens the profile.json file, looks for the player's username stored in the instance,
            and displays their high score
            """
            try:
                with open(PROFILE_FILE, "r") as file:
                    data = json.load(file)
                player_data = next((player for player in data if player["username"].lower() == self.username.lower()), None)
                if player_data:
                    # if player is found display username and high score
                    print(f"Player: {player_data['username']}")
                    print(f"High Score: {player_data['high_score']}")
                else:
                    print(f"Player '{self.username}' not found in the profile data.")
            
            except FileNotFoundError:
                print(f"Error: '{PROFILE_FILE}' not found.")
            except json.JSONDecodeError:
                print(f"Error: '{PROFILE_FILE}' is not a valid JSON file.")
                
                
    def display_history(self):
            """
            Opens the profile.json file, looks for the player's username stored in the instance,
            and displays their history in a table format using tabluate.
            """
            try:
            # Open and load the profile data from JSON
                with open(PROFILE_FILE, "r") as file:
                    data = json.load(file)

                # Find the player data by username
                player_data = next((player for player in data if player["username"].lower() == self.username.lower()), None)
                    # Prepare the table data for tabulate
                    
                if player_data.get("history"):
                            print(f"Player: {player_data['username']} History:")
                            # Prepare table data
                            df = pd.DataFrame(player_data.get("history"))
                            from tabulate import tabulate
                            print(tabulate(df, headers="keys", tablefmt="grid"))
                else:
                    print(f"No history found for player '{username}'.")
                        
            except FileNotFoundError:
                            print(f"Error: '{PROFILE_FILE}' not found.")
            except json.JSONDecodeError:
                            print(f"Error: '{PROFILE_FILE}' is not a valid JSON file.")
            input("Press Enter to continue....")



username = 'Daniel'
player = Player(username)
