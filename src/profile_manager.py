import json
from player import Player

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
                print(f"Your settings are:\nDifficulty: {user.get("difficulty")}\nCategory: {user.get("category")}")
                return Player(
                    username=user.get("username"),
                    difficulty=user.get("difficulty"),
                    category=user.get("category"),
                    high_score=user.get("high_score"),
                    history=user.get("history")
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

# Test the function
if __name__ == "__main__":
    test_player = load_or_create_player("test")
    print(f"Player loaded or created: {test_player}")

