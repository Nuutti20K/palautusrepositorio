from player_reader import PlayerReader


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nation):
        def sort_by_score(player):
                return player.score
        all = self.reader.get_players()
        players = []
        for player in all:
            if player.nationality == nation:
                players.append(player)
        sorted_players = sorted(players, reverse=True, key=sort_by_score)
        return sorted_players