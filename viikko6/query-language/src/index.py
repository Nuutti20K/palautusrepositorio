from statistics import Statistics
from player_reader import PlayerReader
from querybuilder import QueryBuilder
from matchers import And, Or, HasAtLeast, PlaysIn, Not, All, HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )


if __name__ == "__main__":
    main()
