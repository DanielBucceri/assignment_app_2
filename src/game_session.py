from inputimeout import inputimeout, TimeoutOccurred
import requests
from player import Player
import random
import json
from datetime import datetime

TRIVIA_API_URL = "https://opentdb.com/api.php"
PROFILE_FILE = "data/profile.json"

class GameSession:
    def __init__(self, player):
        self.player = player 
        self.timeout = 15
        self.category  = player.category
        self.difficulty = player.difficulty
        
        self.score = 0
        self.incorrect  = 0 
        self.correct = 0
        self.difficulty_point = 1

    def play_game(self):
        params = {
            "amount": 10,
            "category": self.category,
            "difficulty": self.difficulty,
            "type": "multiple"
        }
        try:
            response = requests.get(TRIVIA_API_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            if data["response_code"] == 0:
                questions = data["results"]
                for q in questions:
                    print(f"\nQuestion: {q['question']}")
                    choices = q["incorrect_answers"]
                    choices.append(q["correct_answer"])
                    random.shuffle(choices)
                    for i, option in enumerate(choices, 1):
                        print(f"{i} {option}")
                    try:
                        answer = int(inputimeout(prompt=f"enter choice (1 - 4) You have {self.timeout} seconds..", timeout=self.timeout)) # updated timer for each game mode
                        if option[answer - 1] == q["correct_answer"]:
                            print("Correct!")
                            self.score += self.difficulty_point # update score by amount based on difficulty
                            self.correct += 1
                            return True
                        else:
                            print(f"Wrong! Correct answer: {q['correct_answer']}")
                            self.incorrect += 1
                        return False
                    except (ValueError, IndexError):
                        print("Invalid input. Counted as incorrect.")
                        return False
                    except (TimeoutError):
                         print("Out of time! Counted as incorrect.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while making the API call: {e}")
        except KeyError:
            print("Unexpected response format from the API. Missing expected keys.")
        except json.JSONDecodeError:
            print("Failed to decode json")
        record_game = {
                "score": self.score,
                "correct": self.correct,
                "incorrect": self.incorrect,
                "date": datetime.datetime.now().strftime("%Y-%m-%d")
            }
        with open(PROFILE_FILE, "r") as f:
            data = json.load(f)
            for user in data:
                if user.get("high_score") < self.score:
                    user["high_score"] = self.score
                if self.player.username == user["username"]:
                    user["history"].append(record_game)
        with open(PROFILE_FILE, "w") as f:
            json.dump(data, f, indent=4)
     
    

class MediumGameMode(GameSession):
    def __init__(self, player):
        super().__init__(self, player)
        self.timeout = 10
        self.difficulty_point = 2
        
    def play_game(self):
        super().play_game()
        
class HardGameMode(GameSession):
    def __init__(self, player):
        super().__init__(self, player)
        self.timeout = 7 
        self.difficulty_point = 3
        
    def play_game(self):
        super().play_game()
    
                    