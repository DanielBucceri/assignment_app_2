# Documentation Feedback Log - Trivia Game Project

This log tracks documentation reviews, feedback received, and improvements made.

## File: `game_session.py`

### First `Review

- **Checked By:** Daniel  
- **Date:** 5/3/25  
- **Feedback Given:**
  - Missing docstrings for GameSession, MediumGameMode, and HardGameMode explaining their purpose  
  - Methods inside GameSession don’t have docstrings describing what they do, their parameters, and return values  
  - TRIVIA_API_URL and PROFILE_FILE constants aren’t explained  
- **Assigned Developer:** Daniel  
- **Actions Taken:**
  - Added detailed docstrings for the GameSession classes methods and thier attributes.
  - TRIVIA_API_URL and PROFILE_FILE constants to clarify their usage.
  - Identified and modified bug in invalid input handling in the play_game method. Replaced the original return false (which crash the game on incorrect) with self.incorrect += 1 regiter as incrrect and move on.
- **Date Actioned:**
- 8/3/25

### Second Review
- **Checked By:**  
- **Date:**  
- **Final Feedback:**  
  -  
- **Fix Needed?** Yes / No  
- **Assigned Developer:**  
- **Fix Implemented:**  
- **Final Validation Date:**  
- **Final Status:** Done / Needs Further Review  

---

### First Review File: `player.py`

- **Checked By:**  Daniel
- **Date:**  8/3/25
- **Feedback Given:**  
- load_or_create_player docstring does not describe parameters or return values  
- Player class lacks docstrings describing the purpose of each method  
- Need to clarify what happens when load_or_create_player is called with a non existing username
- Missing explanation of the update_preferences flow  
- display_history does not show a no user found error
- **Assigned Developer:**  Daniel
- **Actions Taken:**  
- 
- **Date Actioned:**  

### Second Review

- **Checked By:**
- **Date:**  
- **Final Feedback:**
  -  
- **Fix Needed?** Yes / No  
- **Assigned Developer:**  
- **Fix Implemented:**  
- **Final Validation Date:**  
- **Final Status:** Done / Needs Further Review  

---

### First Review File: `main.py`

- **Checked By:**  Daniel
- **Date:** 8/3/25
- **Feedback Given:**  
  - main function missing docstring summarizing  responsibilities as entry point, expected input/output, how it loads the player and how it selects a game type.
  - missing documentation in match case explaining what flow is triggered from each case user choice making it hard to debug or modify in the future. Inline comments required for each case describing what is triggered
  - No description of how errors and valdiation are handled. Requires description on process if user inputs invalid info and any feedback given to the user.
- **Assigned Developer:**  Daniel
- **Actions Taken:**  
- **Date Actioned:**  

### Second Review
- **Checked By:**  
- **Date:**  
- **Final Feedback:**  
  -  
- **Fix Needed?** Yes / No  
- **Assigned Developer:**  
- **Fix Implemented:**  
- **Final Validation Date:**  
- **Final Status:** Done / Needs Further Review  

---

### First Review File: `utility.py`

- **Checked By:**  Daniel
- **Date:**  8/03/25
- **Feedback Given:**  
  - current function doctrings are uindescriptive and missing parameters, return values and descriptive behavior explanation
  - missing docstring for read_json()
  - inline comments missing to explain error handling and user feedback on each function
- **Assigned Developer:**  Daniel
- **Actions Taken:**  
- **Date Actioned:**  

### Second Review
- **Checked By:**  
- **Date:**  
- **Final Feedback:**  
  -  
- **Fix Needed?** Yes / No  
- **Assigned Developer:**  
- **Fix Implemented:**  
- **Final Validation Date:**  
- **Final Status:** Done / Needs Further Review  

---

## File: `README.md`

### First Review

- **Checked By:**  Daniel
- **Date:**  8/03/25
- **Feedback Given:**
  - Differences in game modes not clearly described. Eg. "Easy = 15 second time limit and 1 point per correct answer"
  - missing explanation for no "errors found error". Would benfit from an explanation of potential causes and troubleshooting steps
- **Assigned Developer:**  Daniel
- **Actions Taken:**  
- **Date Actioned:**  

### Second Review
- **Checked By:**  
- **Date:**  
- **Final Feedback:**  
  -  
- **Fix Needed?** Yes / No  
- **Assigned Developer:**  
- **Fix Implemented:**  
- **Final Validation Date:**  
- **Final Status:** Done / Needs Further Review  
