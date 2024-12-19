class Game:
    def __init__(self, game_name,) -> None:
        
 #lets use inheritence to create different game types based on difficulty and type. such as extra ppoints for hard questions and different output for true/false
 # composition - we can pass player to game session to have access to preferences adn scores and histroy ?       
class GameSession:
    """
    Represents a single game session, including the current score and
    tracking correct/incorrect answers.
    """
    def __init__(self, player: Player):
        self.player = player
        self.score = 0
        self.correct = 0
        self.incorrect = 0

    def answer_correct(self):
        self.score += 10
        self.correct += 1

    def answer_incorrect(self):
        self.incorrect += 1

    def is_over(self):
        return self.incorrect >= 3


#### Add game result to history and leaderboard if new high score 
    def add_game_result(self, score: int, correct: int, incorrect: int):
        self.history.append({
            "date": datetime.datetime.now().isoformat(),
            "score": score,
            "correct": correct,
            "incorrect": incorrect
        })
        # Keep only last GAME_HISTORY_LIMIT items if needed
        from config import GAME_HISTORY_LIMIT
        if len(self.history) > GAME_HISTORY_LIMIT:
            self.history = self.history[-GAME_HISTORY_LIMIT:]
        if score > self.high_score:
            self.high_score = score
        