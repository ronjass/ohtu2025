import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_olemassaoleva_pelaaja_loytyy(self):
        result = self.stats.search("Kurri")
        self.assertEqual(result.name, "Kurri")

    def test_olematon_pelaaja_ei_loydy(self):
        result = self.stats.search("EiPelaaja")
        self.assertEqual(result, None)

    def test_team_palauttaa_pelaajat(self):
        result = self.stats.team("EDM")
        self.assertEqual(len(result), 3)
        self.assertIn(self.stats.search("Semenko"), result)
        self.assertIn(self.stats.search("Kurri"), result)
        self.assertIn(self.stats.search("Gretzky"), result)

    def test_top_palauttaa_oikeassa_jarjestyksessa(self):
        result = self.stats.top(2)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].name, "Gretzky")
        self.assertEqual(result[1].name, "Lemieux")