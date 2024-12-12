import json
import os

class Player:
    def __init__(self, user_name, difficulty, high_score, history):
        self.user_name = user_name
        self.high_score = high_score
        self.history = history
        self.difficulty = difficulty

    def load_player(self, user_name):
        file_path = "../data/profile.json"

# Use the constructed path directly in open as a string
        with open(file_path, "r") as file:
            profile_data = json.load(file)
            #check if user exists
            if user_name in profile_data:
                print(profile_data[user_name])
                profile = profile_data[user_name]
            return profile



            # user_found = False
            # for user in profile_data:
            #     if user.get('user_name') == user_name:
            #         user_found = True
            #     #load preferences from json
            #     profile = user

            #     if user_found == False:

player = Player(None, None, None, None)

    # Call load_player with 'Alice' (assuming the profile.json file exists)
profile = player.load_player("Alice")

if profile:
        print(f"Profile loaded for {profile['username']}")
        print(f"Difficulty: {profile['difficulty']}")
        print(f"High Score: {profile['high_score']}")
        print(f"History: {profile['history']}")
else:
        print("Player not found.")