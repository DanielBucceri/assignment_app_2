import pandas as pd
from utility import choose_from_menu, read_json, save_json
import json

PROFILE_FILE = "data/profile.json"
LEADERBOARD_FILE = "data/Leaderboard.json"

def load_or_create_player(username):
    """
    Load an existing player by username or create a new one if not found.
    """
    try:
        # Open and load the JSON file
        with open(PROFILE_FILE, "r") as file:
            data = json.load(file)

        # Search for the matching username
        for user in data:
            if user.get("username", "").lower() == username.lower():
                # Return a Player instance initialized with the data
                print(f"welcome {user.get("username")}")
                print(
                    f"Your settings are:\nDifficulty: {user.get("difficulty")}\nCategory: {user.get("category")}"
                )
                return Player(
                    username=user.get("username"),
                    difficulty=user.get("difficulty"),
                    category=user.get("category"),
                    high_score=user.get("high_score"),
                    history=user.get("history"),
                )
        # If username is not found, create a new Player and add defaults to file
        new_player = Player(username)
        data.append(vars(new_player))
        print(f"Player {username} created")

        # Save updated data back to the JSON file
        with open(PROFILE_FILE, "w") as file:
            json.dump(data, file, indent=4)
            return new_player

    except FileNotFoundError:
        print(f"Error: File '{PROFILE_FILE}' not found. Creating profiles.json")
        # Create a default profile structure if the file doesn't exist
        data = []
        new_player = Player(username)
        data.append(vars(new_player))
        with open(PROFILE_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return new_player

    except json.JSONDecodeError:
        print(f"Error: File '{PROFILE_FILE}' is not a valid JSON file.")
        return new_player

class Player:
    def __init__(
        self, username, difficulty="medium", high_score=0,
        category=19, history=[]
    ):
        self.username = username
        self.difficulty = difficulty
        self.category = category
        self.high_score = high_score
        self.history = history

    def update_preferences(self):
        difficulty_input = int(
            input(
                "Enter corresponding number to select difficulty."
                " 1.easy 2.medium 3.hard: "
            )
        )
        match difficulty_input:
            case 1:
                difficulty = "easy"
            case 2:
                difficulty = "medium"
            case 3:
                difficulty = "hard"
            case _:
                difficulty = "medium"
        category = choose_from_menu()
        data = read_json(PROFILE_FILE)  # load json
        for user in data:
            if user.get("username").lower() == self.username.lower():
                # Update only the fields that are provided
                if difficulty:
                    user["difficulty"] = difficulty
                if category:
                    user["category"] = category
                save_json(PROFILE_FILE, data)  # save data back to json

            print(f"Preferences for'{self.username}' updated successfully.")
            return True
        else:
            print(f"User '{self.username}' not found.")
            return False

    def display_high_score(self):
        """
        Opens the profile.json file, looks for the player's
        username stored in the instance,
        and displays their high score
        """
        data = read_json(PROFILE_FILE)
        if data:
            player_data = next(
                (
                    player
                    for player in data
                    if player["username"].lower() == self.username.lower()
                ),
                None,
            )
            if player_data:
                # if player is found display username and high score
                print(f"Player: {player_data['username']}")
                print(f"High Score: {player_data['high_score']}")
            else:
                print(f"Player '{self.username}'"
                      "not found in the profile data.")

    def display_history(self):
        """
        Opens the profile.json file,
        looks for the player's username stored in the instance,
        and displays their history in a table format using tabluate.
        """
        data = read_json(PROFILE_FILE)
        if data:
            # Find the player data by username
            player_data = next(
                (
                    player
                    for player in data
                    if player["username"].lower() == self.username.lower()
                ),
                None,
            )
            # create the table data for tabulate
        if player_data.get("history"):
            print(f"Player: {player_data['username']} History:")
            # Prepare table data
            df = pd.DataFrame(player_data.get("history"))
            from tabulate import tabulate

            print(tabulate(df, headers="keys", tablefmt="grid"))
        else:
            print(f"No history found for player '{self.username}'.")
        input("Press Enter to continue....")

