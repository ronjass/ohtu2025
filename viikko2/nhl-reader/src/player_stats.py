class PlayerStats:
    def __init__(self, reader):
        self._reader = reader

        self._players = self._reader.get_players()

    def top_scorers_by_nationality(self, nat):
        top_players_nat = []

        for player in self._players:
            if player.nationality == nat:
                top_players_nat.append(player)

        return sorted(top_players_nat, key=lambda player: player.assists + player.goals, reverse=True)

    def top_scorers_fin(self):
        top_players_nat = []

        for player in self._players:
            if player.nationality == "FIN":
                top_players_nat.append(player)

        return sorted(top_players_nat, key=lambda player: player.assists + player.goals, reverse=True)
