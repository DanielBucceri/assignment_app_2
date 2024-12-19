# from datetime import datetime

# # class CookieFactory:
# #     total_cookies_made = 0  # Shared across all instances

# #     def __init__(self, flavor):
# #         self.flavor = flavor
# #         CookieFactory.total_cookies_made += 1

# #     # Instance method to get total cookies
# #     def get_total_cookies(self):
# #         return CookieFactory.total_cookies_made

# # # Create cookies
# # cookie1 = CookieFactory("Chocolate")
# # cookie2 = CookieFactory("Vanilla")
# # something = CookieFactory("pee")

# # # Try to get the total cookies using the method
# # print(CookieFactory.get_total_cookies())  # Output: 2

# import requests
# import random
# import html

# def get_trivia_questions(amount=5, difficulty="medium"):
#     """
#     Fetches trivia questions from the Open Trivia Database API.

#     :param amount: Number of questions to fetch
#     :param difficulty: Difficulty level (easy, medium, hard)
#     :return: List of questions
#     """
#     url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data['results']
#     else:
#         print("Failed to fetch questions. Please check your internet connection.")
#         return []

# def play_trivia():
#     print("Welcome to the Trivia Game!")
#     print("You will be asked 5 questions. Try to answer them correctly!")
    
#     questions = get_trivia_questions()
#     if not questions:
#         print("No questions available. Exiting game.")
#         return

#     score = 0

#     for i, question in enumerate(questions):
#         print(f"\nQuestion {i + 1}: {html.unescape(question['question'])}")

#         # Combine correct and incorrect answers, then shuffle
#         options = question['incorrect_answers'] + [question['correct_answer']]
#         random.shuffle(options)

#         for idx, option in enumerate(options, 1):
#             print(f"{idx}. {html.unescape(option)}")

#         while True:
#             try:
#                 answer = int(input("Your answer (1-4): "))
#                 if 1 <= answer <= 4:
#                     break
#                 else:
#                     print("Please enter a number between 1 and 4.")
#             except ValueError:
#                 print("Invalid input. Please enter a number between 1 and 4.")

#         if options[answer - 1] == question['correct_answer']:
#             print("Correct!")
#             score += 1
#         else:
#             print(f"Wrong! The correct answer was: {html.unescape(question['correct_answer'])}")

#     print(f"\nGame Over! Your final score is {score}/{len(questions)}.")

# if __name__ == "__main__":
#     play_trivia()

# import requests
# import json

# # Define the API endpoint URL
# url = 'https://opentdb.com/api.php?amount=10&category=19&difficulty=easy&type=multiple'

# # Make the GET request to the API
# response = requests.get(url)

# # Check if the response is successful
# if response.status_code == 200:
#     data = response.json()  # Parse the JSON response
#     # Debugging: Print the raw JSON response
#     print("Raw API Response:")
#     print(json.dumps(data, indent=4))

#     # Check if 'results' exists and has questions
#     if "results" in data and data["results"]:
#         questions = data["results"]
#         print("\nQuestions Retrieved:")
#         for idx, question in enumerate(questions, start=1):
#             print(f"Question {idx}: {question['question']}")
#             options = question['incorrect_answers'] + [question['correct_answer']]
#             # Shuffle options
#             import random
#             random.shuffle(options)
#             for i, option in enumerate(options, start=1):
#                 print(f"   {i}. {option}")
#             print(f"Correct Answer: {question['correct_answer']}\n")
#     else:
#         print("No questions found in the API response. Check the API query parameters.")
# else:
#     print(f"Request failed with status code {response.status_code}")

import requests
import json
import time


# i = 0
# while i < 10:

#   # Define the API endpoint URL
#   url = 'https://opentdb.com/api.php?amount=1&category=19&difficulty=easy&type=multiple'
#   time.sleep(5)
#   # Make the GET request to the API
#   response = requests.get(url)
  
#   # Check if the response is successful
#   if response.status_code == 200:
#       data = response.json()  # Parse the JSON response
#       print("Request was successful! Here is the response:")
#       print(json.dumps(data['results'][0]['question'], indent=4))  # Pretty print the JSON response
#   else:
#       print(f"Request failed with status code {response.status_code}")

#   i += 1
# import requests
# import time

# response = requests.get("https://opentdb.com/api_count.php?category=9")
# response = response.json() 

# category_qs = response.get('category_question_count')

# total_count = category_qs.get("total_question_count")

# print(total_count)
# from tabulate import tabulate
# import json
# PROFILE_FILE = "data/profile.json"
# LEADERBOARD_FILE = "data/Leaderboard.json"

# def display_history(username):
#         """
#         Opens the profile.json file, looks for the player's username stored in the instance,
#         and displays their history in a table format using tabluate.
#         """
#             # Open and load the profile data from JSON
#         with open(PROFILE_FILE, "r") as file:
#             data = json.load(file)

#             # Find the player data by username
#         player_data = next((player for player in data if player["username"].lower() == username.lower()), None)

#         if player_data and player_data.get("history"):
#                 # Prepare table data
#                 headers = ["Score", "Correct Answers", "Incorrect Answers", "Date"]
#                 print(tabulate(player_data.get("history"), headers, tablefmt='grid'))
            
            
# print(display_history("Daniel"))


from tabulate import tabulate
import json
import pandas as pd
PROFILE_FILE = "data/profile.json"
LEADERBOARD_FILE = "data/Leaderboard.json"
from tabulate import tabulate

def display_leaderboard_as_table(json_file):

    try:
        # Read the JSON file
        with open(json_file, 'r') as file:
            data = json.load(file)

        # Check if data is a list of dictionaries
        if not isinstance(data, list):
            
            return print("Invalid Json.")

        # Create a DataFrame from the data
        df = pd.DataFrame(data)

        # Use tabulate to print the DataFrame as a table
        print(tabulate(df, headers='keys', tablefmt='grid'))

    except FileNotFoundError:
        print(f"Error: File '{json_file}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{json_file}' is not valid Json .")

# Example usage
if __name__ == "__main__":
    display_leaderboard_as_table(LEADERBOARD_FILE)

# def display_history(username):
#     """
#     Opens the profile.json file, looks for the player's username stored in the parameter,
#     and displays their history in a table format using tabulate.
#     """
#     # Open and load the profile data from JSON
#     with open(PROFILE_FILE, "r") as file:
#         data = json.load(file)

#     # Find the player data by username
#     player_data = next((player for player in data if player["username"].lower() == username.lower()), None)
#         # Prepare the table data for tabulate
        
#     if player_data.get("history"):
#                 # Prepare table data
#                 df = pd.DataFrame(player_data.get("history"))
#                 from tabulate import tabulate
#                 print(tabulate(df, headers="keys", tablefmt="grid"))
#     else:
#         print(f"No history found for player '{username}'.")

# # Example usage
# display_history("Daniel")


