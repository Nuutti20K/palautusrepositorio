import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.reader = PlayerReaderStub()
        self.stats = StatisticsService(self.reader)

    def test_finds_player(self):
        player = self.stats.search("Semenko")

        self.assertEqual(player.__str__(), f"Semenko EDM 4 + 12 = 16")

    def test_player_does_not_exist(self):
        player = self.stats.search("Jaska")

        self.assertEqual(player, None)

    def test_players_of_team(self):
        players = self.stats.team("EDM")

        correct = [
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ]

        for i in range(len(players)):
            self.assertEqual(players[i].__str__(), correct[i].__str__())

    def test_top_players(self):
        players = self.stats.top(2)

        correct = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]

        for i in range(len(players)):
            self.assertEqual(players[i].__str__(), correct[i].__str__())
