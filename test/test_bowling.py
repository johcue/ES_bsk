import unittest
from src.frame import Frame
from src.bowling import BowlingGame
from src.bowling_error import BowlingError

class TestBowlingGame(unittest.TestCase):

    def test_create_game(self):
        f = Frame(1,5)
        game = BowlingGame()
        game.add_frame(f)
        self.assertEqual(f, game.get_frame_at(0))

    def test_empty_game(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at,0)

