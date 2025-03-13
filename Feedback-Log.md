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

- **Checked By:**  Daniel
- **Date:**  12/3/25
- **Final Feedback:**  
- Docstrings for GameSession, MediumGameMode, and HardGameMode are now present and clearly describe their purpose.  
- Method docstrings in GameSession now describe functionality, parameters, and return values.  
- TRIVIA_API_URL and PROFILE_FILE constants now have explanations clarifying their usage.  
- Invalid input handling bug in play_game method is now fixed. The incorrect input no longer crashes the game and is correctly counted as an incorrect answer.  

- **Fix Needed?** Yes / No  | No
- **Assigned Developer:**  
- **Fix Implemented:**  
- **Final Validation Date:**  
- **Final Status:** Done / Needs Further Review  | Done

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
  - All requested fixes have been correctly implemented
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
  - expand on invalid input error and user prompt to better clarity
- **Assigned Developer:**  Daniel
- **Actions Taken:**  
- Added a docstring to the main function summarizing its role as the entry point, expected input/output, player loading process, and game type selection.  
- Added inline comments in the match case to explain the flow triggered by each user choice, improving readability and ease of debugging.  
- Documented how errors and validation are handled, including the process for handling invalid user input and the feedback provided to the user.  

- **Date Actioned:**  

### Second Review

- **Checked By:** Daniel
- **Date:**  12/3/25
- **Final Feedback:**  
- The main function now includes a clear docstring summarizing its responsibilities, expected input/output, player loading process, and game type selection.  
- Inline comments have been added in the match case, explaining what each user choice triggers, making it easier to debug and modify.  
- Error handling and invalid input responses have been clarified, improving user guidance and validation.  
- **Fix Needed?** Yes / No | No
- **Assigned Developer:**  
- **Fix Implemented:**  
- **Final Validation Date:** 12/3/25
- **Final Status:** Done / Needs Further Review  | No

---

### First Review File: `utility.py`

- **Checked By:**  Daniel
- **Date:**  8/03/25
- **Feedback Given:**  
- Missing docstrings for read_json and save_json functions explaining their purpose and expected behavior.
- display_leaderboard function lacks a docstring detailing its process, including sorting, writing to a file, and displaying data.
- No explanation of PROFILE_FILE and LEADERBOARD_FILE constants.  
- choose_from_menu function should clarify its return values selected category name and corresponding number.  

- **Assigned Developer:**  Daniel
- **Actions Taken:**  
- Added detailed docstrings to choose_from_menu, display_leaderboard, read_json, and save_json, specifying their purpose, expected inputs/outputs, and error handling behavior.
- Clarified the purpose of PROFILE_FILE and LEADERBOARD_FILE constants with inline comments.
- Updated choose_from_menu to specify that it returns a tuple containing the selected category name and category number.
- Updated display_leaderboard to clearly document the process of loading data, building the leaderboard, sorting it, writing to a file, and displaying the results.

- **Date Actioned:**  13/3/25

### Second Review
- **Checked By:** Daniel
- **Date:**  13/3/25
- **Final Feedback:**
- Docstrings for all functions are now present and correctly describe their purpose, inputs, and outputs.  
- PROFILE_FILE and LEADERBOARD_FILE constants are defined but still do not have inline comments explaining their role  
- In read_json exception messages incorrectly reference PROFILE_FILE instead of using the actual file parameter in case of error with the leaderboar.json.  
- **Fix Needed?** Yes / No  | Yes
- **Assigned Developer:**  Daniel
- **Fix Implemented:**  
- PROFILE_FILE and LEADERBOARD_FILE constants now include inline comments explaining their role
- rea_json exception message now shows the correct file path trying to be passed in.
- **Final Validation Date:**  13/3/25
- **Final Status:** Done / Needs Further Review  | done

---

## File: `README.md`

### First Review

- **Checked By:**  Daniel
- **Date:**  8/03/25
- **Feedback Given:**
  - Differences in game modes not clearly described. Eg. "Easy = 15 second time limit and 1 point per correct answer"
  - missing explanation for "no questions found error". Would benfit from an explanation of potential causes and troubleshooting steps
  - Missing descriptions for imported packages, making it unclear why each dependency is required.
  - User data section does not specify where data is stored or how users can delete/reset their profiles. Needs a clear explanation of profile.json storage, usage, and deletion instructions.  
  - No license declaration in the README. Needs a License section to clarify under what terms the project can be used or modified.  
  - No clear problem statement or target audience.
  - differences from existing trivia platforms not defined.
- **Assigned Developer:**  Daniel
- **Actions Taken:**
- Added a game mode breakdown in the Usage section, detailing time limits and scoring.  
- Explained the "No Questions Found" error in Troubleshooting, listing causes and solutions.  
- Described each imported package in the Third-Party Libraries and Licenses section.  
- Clarified User Data storage, collected information, and profile deletion steps.  
- Added a License section specifying MIT License terms and usage rights.  
- Defined the target audience and problem statement.  
- Highlighted differences from platforms like Kahoot, emphasizing offline play and local tracking.  
- **Date Actioned:** 12/3/25

### Second Review

- **Checked By:** Daniel
- **Date:**  
- **Final Feedback:**
- Differences in game modes are now clearly described under Game Modes.  
- Explanation for "No Questions Found" error is now in troubleshooting, detailing potential causes and solutions.  
- Descriptions for imported packages have been added under third party Libraries and Licenses, clarifying their purpose.  
- User data storage and deletion/reset process is now clearly outlined in User Data.  
- License declaration is now present under License, specifying MIT terms.  
- Clear problem statement and target audience have been added under target users & problem statement.  
- Differences from existing trivia platforms are now explained in how this differs from similar projects.  
- **Fix Needed?** Yes / No  | no
- **Assigned Developer:**  Daniel
- **Fix Implemented:**  
- **Final Validation Date:**  12/3/25
- **Final Status:** Done / Needs Further Review  | Done

### Review Process (Kanban Flow in GitHub)

For tracking reviews and fixes, we can use GitHub Kanban projects:

Issue Creation: A separate issue is created for each file to be reviewed.
Review Branch: The reviewer creates a branch, conducts the review, and pushes changes.
Review Status: The branch is moved to "Reviewed" in the Kanban board.
Development Fixes: The developer pulls the branch, moves it to "In Progress", makes necessary changes, commits, and pushes.
Request Review: Once fixes are made, the branch moves to "Request Review" for final verification.
Final Check: The reviewer does a final check.
If approved, the branch is merged and moved to "Done".
If additional changes are required, the branch moves back to "Reviewed" with comment
