from rich.console import Console
from rich.table import Table
from rich.text import Text
from player_reader import PlayerReader
from player_stats import PlayerStats

def get_user_input():
    country = input("Enter the country (e.g. FIN): ").strip().upper()
    season = input("Enter the season (e.g. 2024-25): ").strip()
    return country, season

def create_table(players, season, country):
    table = Table(title=f"Season {season} players from {country}")

    columns = [("Released", "left"), ("teams", "left"), ("goals", "right"), ("assists", "right"), ("points", "right")]
    for column, justify in columns:
        table.add_column(column, justify=justify)

    for player in players:
        name = Text(player.name, style="blue")
        team = Text(str(player.team), style="red")
        goals = Text(str(player.goals), style="green")
        assists = Text(str(player.assists), style="green")
        points = Text(str(player.assists + player.goals), style="green")
        table.add_row(name, team, goals, assists, points)

    return table

def main():
    country, season = get_user_input()
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(country)

    table = create_table(players, season, country)

    console = Console()
    console.print(table)

if __name__ == "__main__":
    main()
