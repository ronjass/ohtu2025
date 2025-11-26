class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str) -> None:
        if player_name == "player1":
            self.player1_score += 1
        elif player_name == "player2":
            self.player2_score += 1

    def get_score(self) -> str:
        if self.player1_score == self.player2_score:
            return self.get_tied_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_advantage_or_win_score()
        else:
            return self.get_running_score()

    def get_tied_score(self) -> str:
        if self.player1_score < 3:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"
        return "Deuce"

    def get_advantage_or_win_score(self) -> str:
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def get_running_score(self) -> str:
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
