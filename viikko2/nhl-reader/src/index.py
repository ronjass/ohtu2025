from player import Player
from player_reader import PlayerReader
from player_stats import PlayerStats
from rich.console import Console
from rich.table import Table
from rich.text import Text

def main():
    country = input("Enter the country (e.g. FIN): ").strip().upper()
    season = input("Enter the season (e.g. 2024-25): ").strip()

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(country)

    console = Console()
    
    table = Table(title=f"Season {season} players from {country}")

    # Lisää sarakkeet
    table.add_column("Released", justify="left")
    table.add_column("teams", justify="left")
    table.add_column("goals", justify="right")
    table.add_column("assists", justify="right")
    table.add_column("points", justify="right")

    for player in players:
        name = Text(player.name, style="blue") 
        team = Text(str(player.team), style="red")
        goals = Text(str(player.goals), style="green")
        assists = Text(str(player.assists), style="green")
        points = Text(str(player.assists+player.goals), style="green")
        table.add_row(name, team, goals, assists, points)

    console.print(table)
        
if __name__ == "__main__":
    main()
