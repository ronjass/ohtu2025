import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url, timeout=10)
        response.raise_for_status()
        response_players = response.json()
        players = []

        for player_dict in response_players:
            player = Player(player_dict)
            players.append(player)

        return players

    def player_count(self):
        players = self.get_players()
        return len(players)
