from rich import print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    while True:
        print("[italic]NHL statistics by nationality\n")

        seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", ""]
        season = Prompt.ask("Select season", choices=seasons)
        if season == "":
            return
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"

        nations = ["AUT","CZE","AUS","SWE","GER","DEN","SUI","SVK","NOR","RUS","CAN","LAT","BLR","SLO","USA","FIN","GBR"]
        nation = Prompt.ask("Select season", choices=nations)

        table = Table(title=f"Top scorers of {nation} season {season}")


        table.add_column("name", justify="left", style="white", no_wrap=True)
        table.add_column("team", justify="left", style="white", no_wrap=True)
        table.add_column("goals", justify="left", style="white", no_wrap=True)
        table.add_column("assists", justify="left", style="white", no_wrap=True)
        table.add_column("points", justify="left", style="white", no_wrap=True)

        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nation)

        for player in players:
            table.add_row(f"[cyan]{str(player.name)}", f"[magenta]{str(player.team)}", f"[green]{str(player.goals)}", f"[green]{str(player.assists)}", f"[green]{str(player.score)}")

        console = Console()
        console.print(table)
        

if __name__ == "__main__":
    main()
