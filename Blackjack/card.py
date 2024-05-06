#!/usr/bin/env python3
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rank_names = {
            1: "Ace",
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        rank_name = rank_names.get(self.rank, str(self.rank))
        suit_names = {
            'C': 'Clubs',
            'D': 'Diamonds',
            'H': 'Hearts',
            'S': 'Spades'
        }
        suit_name = suit_names.get(self.suit, self.suit)
        return f"{rank_name} of {suit_name}"

