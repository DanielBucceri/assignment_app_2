from inputimeout import inputimeout, TimeoutOccurred
import requests
import random
import json
from datetime import datetime
from utility import read_json, save_json
import html

# API endpoint for pulling trivia questions from the api
TRIVIA_API_URL = "https://opentdb.com/api.php"

# Path to the profile JSON file storing player data
PROFILE_FILE = "data/profile.json"


class GameSession:
    """
    Handles a game session for a player.

    Attributes:
        player (class): The player object.
        timeout (int): Time limit for answering a question (based on difficulty).
        category (int): The category of questions pulled in.
        difficulty (str): The difficulty level. Pulled in from player profile json if set otherwise default value
        score (int): Players score for the session. Incremented points based on correct questions answered and diffuculty
        incorrect (int): Number of incorrect answers.
        correct (int): Number of correct answers.
        difficulty_point (int): Points per correct answer based on difficulty.
    """
    def __init__(self, player):
        """
    Initializes a GameSession instance.

    Args: player (Player): Loads the player class, pulling in profile preferences.
        """
        self.player = player
        self.timeout = 15
        self.category = player.category
        self.difficulty = player.difficulty

        self.score = 0
        self.incorrect = 0
        self.correct = 0
        self.difficulty_point = 1

    def play_game(self):
        """
    Starts the game, fetching and presenting questions based on user profile.

    Retrieves 10 or more trivia questions based on the players selected category
    and difficulty. Handles user input for answers and keeps track of
    scores, correct/incorrect responses, and updates player history.

    Returns: None
    """
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
                        self.incorrect += 1 
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
    """
    Inherited from GameSession class. Medium difficulty settings applied.
    Overwrites to increases GameSession timeout and difficulty_point.
    """
    def __init__(self, player):
        super().__init__(player)
        self.timeout = 10
        self.difficulty_point = 2

    def play_game(self):
        super().play_game()


class HardGameMode(GameSession):
    """
    Inherited from GameSession class. Hard difficulty settings applied.
    Overwrites to increase GameSession timeout and difficulty_point.
    """
    def __init__(self, player):
        super().__init__(player)
        self.timeout = 7
        self.difficulty_point = 3

    def play_game(self):
        super().play_game()
