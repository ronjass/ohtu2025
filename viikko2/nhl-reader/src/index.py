import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    fin_players = []

    for player in players:
        if player.nationality == "FIN":
            fin_players.append(player)

    print("Players from FIN:")
    print()

    for player in sorted(fin_players, key=lambda player: player.assists + player.goals, reverse=True):
        print(player)
        
if __name__ == "__main__":
    main()
