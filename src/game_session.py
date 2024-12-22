from inputimeout import inputimeout, TimeoutOccurred
import requests
import random
import json
from datetime import datetime
from utility import read_json, save_json
import html

TRIVIA_API_URL = "https://opentdb.com/api.php"
PROFILE_FILE = "data/profile.json"


class GameSession:
    def __init__(self, player):
        self.player = player
        self.timeout = 15
        self.category = player.category
        self.difficulty = player.difficulty

        self.score = 0
        self.incorrect = 0
        self.correct = 0
        self.difficulty_point = 1

    def play_game(self):
        params = {
            "amount": 10,
            "category": self.category,
            "difficulty": self.difficulty,
            "type": "multiple",
        }
        try:
            response = requests.get(TRIVIA_API_URL, params=params, timeout=5)
            response.raise_for_status()
            data = response.json()
            if data["response_code"] == 0:
                questions = data["results"]
                print(f"\nGame started. Difficulty: {self.difficulty} timeout: {self.timeout} Question point: {self.difficulty_point}")
                for q in questions:
                    question = html.unescape(q['question']) #remove &quot; appearing in strings
                    print(f"\nQuestion: {question}")
                    choices = q["incorrect_answers"]
                    choices.append(q["correct_answer"])
                    random.shuffle(choices)
                    for i, option in enumerate(choices, 1):
                        print(f"{i} {option}")
                    try:
                        answer = int(inputimeout(prompt=f"enter choice (1 - 4) You have {self.timeout} seconds: ",timeout=self.timeout,))  # updated timer for each game mode
                        if choices[answer - 1] == q["correct_answer"]:
                            print("Correct!")
                            self.score += (
                                self.difficulty_point
                            )  # update score by amount based on difficulty
                            self.correct += 1 
                        else:
                            print(f"Wrong! Correct answer: {q['correct_answer']}")
                            self.incorrect += 1
                    except (ValueError, IndexError):
                        print("Invalid input. Counted as incorrect.")
                        return False
                    except TimeoutOccurred:
                        print("\nOut of time! Counted as incorrect.")
            if data["response_code"] == 1:
                print("No questions found for your criteria. Try changing category or difficulty.")
                return
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while making the API call: {e}")
        except KeyError:
            print("Unexpected response format from the API. Missing expected keys.")
        except json.JSONDecodeError:
            print("Failed to decode json")
        data = read_json(PROFILE_FILE)
        for user in data:
            if user.get("username") == self.player.username:
                if user.get("high_score") < self.score:
                    user["high_score"] = self.score
                    print(f"Game over.\nNew high score! {self.score}. Correct: {self.correct} incorrect: {self.incorrect}")
                else: 
                    print(f"Game over. You scored {self.score} points. Correct: {self.correct} incorrect: {self.incorrect}")
                if self.player.username == user["username"]:
                    record_game = {
                "score": self.score,
                "correct": self.correct,
                "incorrect": self.incorrect,
                "date": datetime.now().strftime("%Y-%m-%d"),
            }
                    user["history"].append(record_game)
                    save_json(PROFILE_FILE, data)
        
       


class MediumGameMode(GameSession):
    def __init__(self, player):
        super().__init__(player)
        self.timeout = 10
        self.difficulty_point = 2

    def play_game(self):
        super().play_game()


class HardGameMode(GameSession):
    def __init__(self, player):
        super().__init__(player)
        self.timeout = 7
        self.difficulty_point = 3

    def play_game(self):
        super().play_game()
