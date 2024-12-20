from player import Player
from profile_manager import load_or_create_player
from utility import display_leaderboard
from game_session import GameSession


def main():
    username = input("Enter your username: ").strip()
    player = load_or_create_player(username)
    game = GameSession(player)

    while True:
        print("\n1. Play Game\n2. Update Preferences\n3. View Leaderboard\n4. View History\n5. See high score\n6. Quit game")
        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                game.play_game() 
            case "2":
                player.update_preferences()
            case "3":
                display_leaderboard()
            case "4":
                player.display_history()
            case "5":
                player.display_high_score()
            case "6":
                print("Cya!")
                break
            case _:
                print("Invalid choice.")
                
                
if __name__ == "__main__":
    main()  