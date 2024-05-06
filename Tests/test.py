#!/usr/bin/env python3

import sys
import os
import unittest

blackjack_dir = "/home/malhosani/Desktop/Proj2-Blackjack/Blackjack"
sys.path.append(blackjack_dir)

from blackjack import BlackJackGame

class TestBlackJackGame(unittest.TestCase):
    def test_play_game(self):
        # Test the play of BlackJackGame
        game = BlackJackGame(3)
        game.play()
        self.assertIn(game.winner, [player.name for player in game.players])

if __name__ == '__main__':
    unittest.main()

