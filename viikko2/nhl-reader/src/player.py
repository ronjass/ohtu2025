class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.team = player_dict['team']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.games = player_dict['games']

    def total_points(self):
        return self.goals + self.assists

    def __str__(self):
        return f"{self.name:20} {self.team:20} {self.goals} + {self.assists} = {self.goals + self.assists}"
