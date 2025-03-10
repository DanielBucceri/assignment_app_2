# Trivia Game Application

## Overview

Welcome to the Trivia Game Application! This project is a CLI trivia game using the Open Trivia DB API where players can answer questions, track scores, and compete on a leaderboard. Players can also set preferences such as question categories and difficulty levels for different game modes.

## Features

- Interactive trivia game with multiple difficulty levels.
- Personalized player profiles with history tracking.
- leaderboard to showcase top scores.
- Integration with Open Trivia API for questions.
- Json file based storage for profiles and scores.

## important

-Some categories and difficulty levels may have limited questions. Experiment with different preferences if no questions are returned.
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

### Ethical Considerations

1. ### Third-Party Libraries and Licenses

This project uses the following third-party libraries:

1. **pandas**  
   - License: BSD 3-Clause License  
   - <https://github.com/pandas-dev/pandas/blob/main/LICENSE>

2. **tabulate**  
   - License: MIT License  
   - <https://pypi.org/project/tabulate>

3. **requests**  
   - License: Apache 2.0 License  
   - <https://github.com/psf/requests/blob/main/LICENSE>

4. **inputimeout**  
   - License: MIT License  
   - <https://pypi.org/project/inputimeout/>

### Ethical and Legal Compliance

All third-party libraries are used in compliance with their respective licenses. The project is non-commercial and educational, which aligns with the permissions defined by these licenses.

1. **User Data**:

   - User data is stored locally in `profile.json`.
   - No personally identifiable information is collected or shared with third parties.
   - Users can delete their data by removing the `profile.json` file.

2. **API Usage**:

   - This application uses the Open Trivia Database API (<https://opentdb.com/>) in compliance with its terms of use.
   - API requests are limited to 10 questions at a time avoid overloading the service.

## System Requirements

- Python 3.8+
- Operating System: Windows, macOS, or Linux
- Internet connection for API access

## Troubleshooting

- **Error: File Not Found**:
 Ensure `profile.json` and `Leaderboard.json` exist in the `data/` folder.
- **Invalid Input**: Follow user prompts carefully to avoid input errors.
- **API Timeout**: Ensure a stable internet connection.
- **no questions found error**
