import pandas as pd
from utility import choose_from_menu, read_json, save_json

PROFILE_FILE = "data/profile.json"
LEADERBOARD_FILE = "data/Leaderboard.json"

def load_or_create_player(username):
    """
    Load an existing player by username from JSON or create a new one if not found.
    
    Parameters: 
     username (str): Username of the player.

    Returns:
     Player: The loaded player if existing username found or a newly created one with default value preferences.
    
    """
    data = read_json(PROFILE_FILE)
    # Search for the matching username
    for user in data:
        if user.get("username", "").lower() == username.lower():
            # Return a Player instance initialized with the data
            print(f"\nWelcome {user.get('username')}")
            print(
                f"Your settings are:\nDifficulty: {user.get('difficulty')}\nCategory: {user.get('category')}"
            )
            return Player(
                username=user.get("username"),
                difficulty=user.get("difficulty"),
                category=user.get("category"),
                high_score=user.get("high_score"),
                history=user.get("history"),
            )
            
    # If username is not found, create a new Player
    new_player = Player(username)
    data.append(vars(new_player))
    print(f"\nPlayer {username} created.")

    # Save the updated data using save_json
    save_json(PROFILE_FILE, data)
    return new_player

class Player:
    """
    Represents a player in the game.

    Attributes:
     username (str): The players username.
     difficulty (str): The difficulty level preference.
     category (int): The category ID for the chosen questions category.
     high_score (int): The player's highest recorded  stored in json.
     history (list): A list of dictionaries representing past game results.
    """
    def __init__(
        self, username, difficulty="medium", high_score=0, category=19, history=[]):
        self.username = username
        self.difficulty = difficulty
        self.category = category
        self.high_score = high_score
        self.history = history

    def update_preferences(self):
        """
        Updates the players game preferences.

        Prompts the user to select a difficulty level and category,
        then updates the stored player preferences in the profile JSON.

        Returns:
        - bool: True if update is successful, False if the user is not found.
        """
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

            print(f"\nPreferences for'{self.username}' updated successfully.")
            return True
        else:
            print(f"User '{self.username}' not found.")
            return False

    def display_high_score(self):
        """
        Opens the profile.json file, looks for the players
        username stored in the Json file,
        and displays their high score if found else displays an error message.
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
                print(f"\nPlayer: {player_data['username']}")
                print(f"High Score: {player_data['high_score']}")
            else:
                print(f"Player '{self.username}'"
                      "not found in the profile data.")

    def display_history(self):
        """
        Opens the profile.json file,
        looks for the players username stored in the instance,
        and displays their history in a table format using tabluate. If not found displays an error message.
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
        if not player_data:
            print(f"\nError: Player '{self.username}' not found in profile data.")
            return  # Exit function early if player is missing

        if player_data.get("history"):
            print(f"\nPlayer: {player_data['username']}\nHistory:")
            df = pd.DataFrame(player_data.get("history"))
            from tabulate import tabulate
            print(tabulate(df, headers="keys", tablefmt="grid"))
        else:
            print(f"\nNo history found for player '{self.username}'.")
            
    input("\nPress Enter to continue....")




