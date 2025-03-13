from player import load_or_create_player
from utility import display_leaderboard
from game_session import GameSession, MediumGameMode, HardGameMode


def main():
    """
    Main function to run the game.
    
    -asks player to enter their username then loads or creates a player
    -instantiates a game session based on the player's difficulty level
    -displays a menu for the player to choose an option  yo play the game, update preferences, display leaderboard, display history, display high score, or quits the game
    
    Expected inputs:
    - username: str
    - menu choice: str corresponding to the menu options
    
    Outpus:
    - prints the game menu
    - prints the leaderboard
    - prints the players history
    - prints the players high score
    
    Error handling:
    - if an invalid choice is entered, the function prints "Invalid choice" and prompts the user to enter a valid choice
    
    """
    #asks the user to enter a username and remove extra spaces
    username = input("Enter your username: ").strip()
    
    #loads existing player or creates a new player
    player = load_or_create_player(username)
    
    #instantiate game session based on difficulty else default game
    if player.difficulty.lower() == "medium":
        game = MediumGameMode(player)
    elif player.difficulty.lower() == "hard":
        game = HardGameMode(player)
    else:
        game = GameSession(player)

    while True:
        print(
            "\n1. Play Game\n2. Update Preferences\n3. View Leaderboard\n"
            "4. View History\n5. See high score\n6. Quit game\n"
        )
        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                # Start a game session based on the chosen difficulty
                game.play_game()
            case "2":
                 # Allow the player to update their preferences in the profile.json e.g difficulty, category
                player.update_preferences()
            case "3":
                # Display the leaderboard.json with top player scores
                display_leaderboard()
            case "4":
                # Show the player's game history from profile.json, including past scores and games played
                player.display_history()
            case "5":
                # Display the players highest score from profile.json
                player.display_high_score()
            case "6":
                # Exit the game loop and ends the session
                print("Cya!")
                break
            case _:
                # Handle invalid input and prompt the user again
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
