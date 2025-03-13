# Trivia Game Application

## Overview

Welcome to the Trivia Game Application! This project is a CLI trivia game using the Open Trivia DB API where players can answer questions, track scores, and compete on a leaderboard. Players can also set preferences such as question categories and difficulty levels for different game modes.

## Target Users & Problem Statement

This application is developed for trivia enthusiasts, students, and work scoials who want an easy to setup offline, customizable trivia experience with score tracking. Unlike some online trivia platforms, this game allows users to track personal progress over time and customize categories and difficulty while mainting complete control over your data

## Features

- Interactive trivia game with multiple difficulty levels.
- Personalized player profiles with history tracking.
- leaderboard to showcase top scores.
- Integration with Open Trivia API for questions.
- Json file based storage for profiles and scores.

### Game Modes  

- **Easy:** 15-second time limit, 1 point per correct answer  
- **Medium:** 10-second time limit, 2 points per correct answer  
- **Hard:** 5-second time limit, 3 points per correct answer  

## How This Differs from Similar Projects

Unlike Kahoot or QuizUp, which are primarily online multiplayer trivia platforms, this game is focused on single player gameplay with offline progress tracking. While Kahoot requires an internet connection for every session, this application lets players store their scores locally and track their own improvement over time.

## important

- Some categories and difficulty levels may have limited questions. Experiment with different preferences if no questions are returned.
Boolean game mode has been removed due to the very limited number of available questions.

## Installation

### Prerequisites

1. Python 3.8 or above.
2. Required libraries:
   - `requests`
   - `pandas`
   - `tabulate`
   - `inputimeout`

### Steps

1. Clone or download the project folder.
2. Navigate to the project directory in your terminal:

   ```bash

   cd path/to/project
   ```

3. Install required packages using requirments.txt:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python src/main.py
   ```

## Usage

1. **Start the Game:**
 Enter your username to create or load a profile.
2. **Choose Actions:**
 Select from options to play, update preferences, view leaderboard, or check your high score and history.
3. **Play Trivia:**
 Answer questions within the time limit to score points and update your high score. Shorter time limits and higher points depending on difficulty level

## File Structure

- **`data/`**: Stores player profiles (`profile.json`) and leaderboard data (`Leaderboard.json`).
- **`src/`**: Contains Python modules for game functionality:
  - `main.py`: Entry point.
  - `player.py`: Manages player profiles and preferences.
  - `game_session.py`: Handles game logic and gameplay.
  - `utility.py`: Provides utility functions like leaderboard display.

## User Stories

- "As a trivia player, I want to track my high scores to measure my progress over time."
- "As a competitive user, I want a leaderboard so I can compare my performance with others."
- "As a new player, I want an easy way to adjust game settings so I can personalize my experience."

### Ethical Considerations

### Third-Party Libraries and Licenses

This project uses the following third-party libraries:

**pandas**  

- License: BSD 3-Clause License
- <https://github.com/pandas-dev/pandas/blob/main/LICENSE>
- Purpose: Used for managing and displaying player history and leaderboard data in a structured format.  

**tabulate**  

- License: MIT License
- <https://pypi.org/project/tabulate>
- Purpose: Formats leaderboard and history data for a user-friendly CLI table display.

**requests**  

- License: Apache 2.0 License
- <https://github.com/psf/requests/blob/main/LICENSE>
- Purpose: Handles API calls to fetch trivia questions from Open Trivia DB.

**inputimeout**  

- License: MIT License  
- <https://pypi.org/project/inputimeout/>
- Purpose: Implements a countdown timer for answering questions based on difficulty level.

### Ethical and Legal Compliance

All third-party libraries are used in compliance with their respective licenses. The project is non-commercial and educational, which aligns with the permissions defined by these licenses.

**User Data**:

- User data is stored locally in `profile.json`.
- No personally identifiable information is collected or shared with third parties. Data collected includes: Player username, difficulty settings, high scores and game history.
- Users can delete their data by removing the `profile.json` file.

**API Usage**:

- This application uses the Open Trivia Database API (<https://opentdb.com/>) in compliance with its terms of use.
- API requests are limited to 10 questions at a time avoid overloading the service.

## License  

This project is licensed under the MIT License.  
You are free to use, modify, and distribute this software

## System Requirements

- Python 3.8+
- Operating System: Windows, macOS, or Linux
- Internet connection for API access

## Troubleshooting

**Error: File Not Found**

- Ensure `profile.json` and `Leaderboard.json` exist in the `data/` folder.
- If missing, the game automatically generates a new, empty profile file upon startup
**Corrupted Profile or Leaderboard Data:**  
  - If data is corrupted, copy and delete `profile.json` and restart the game. A fresh profile will be created but history and preferences will be lost. Paste the copied data into the file to attempt recovery
**Invalid Input**
- Follow user prompts carefully to avoid input errors. If choices are 1 - 5, entering 6 will trigger an incorrect answer or error in other isntances of the app.
**API Timeout**
- Ensure a stable internet connection.
**no questions found error**
- Check your internet connection as API access is required.
- Try changing the question category or difficulty combinations, as some combinations have limited avaliable questions or none
