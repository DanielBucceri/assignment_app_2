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
- **Date Actioned:**  11/3/25
- Updated load_or_create_player docstring to include parameter, return type details and clarify username case insensitivity
- Added detailed docstrings for all Player class methods update_preferences, display_high_score and display_history
- clarified when load_or_create_player is called with a non existing username new user is created with default settings
- Expanded the update_preferences docstring to describe the exact user prompts and JSON updating flow
- fixed bug in display_history converting username to lower. Usernames are case sensitive. removed .toLower
- Corrected display_history method to include error handling and message for the scenario where a user isn't found in the JSON file
- Committed all changes to the player.py_review branch, pushed to GitHub, and moved the issue into "Request Review" column in the Kanban project for final review

### Second Review

- **Checked By:** Daniel
- **Date:**  11/5/25
- **Final Feedback:**
  -  All requested fixes have been correctly implemented
  - Docstrings are now clear and properly describe function behavior
  - Error handling in display_history is implemented, preventing incorrect lookups
  - Username case sensitivity is now correctly handled
- **Fix Needed?** No  
- **Assigned Developer:**  
- **Fix Implemented:**  
- **Final Validation Date:**  
- **Final Status:** Done / Needs Further Review  | Done

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


Review Process (Kanban Flow in GitHub)
For tracking reviews and fixes, we can use GitHub Kanban projects:

Issue Creation: A separate issue is created for each file to be reviewed.
Review Branch: The reviewer creates a branch, conducts the review, and pushes changes.
Review Status: The branch is moved to "Reviewed" in the Kanban board.
Development Fixes: The developer pulls the branch, moves it to "In Progress", makes necessary changes, commits, and pushes.
Request Review: Once fixes are made, the branch moves to "Request Review" for final verification.
Final Check: The reviewer does a final check.
If approved, the branch is merged and moved to "Done".
If additional changes are required, the branch moves back to "Reviewed" with comments.