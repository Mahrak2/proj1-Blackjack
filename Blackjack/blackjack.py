import random
from player import HumanPlayer, AIPlayer
from card import Card

class BlackJackGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []
        for i in range(num_players):
            player_type = input(f"Enter player {i+1}'s type (human/ai): ").lower()
            name = input(f"Enter player {i+1}'s name: ")
            if player_type == 'human':
                player = HumanPlayer(name)
            elif player_type == 'ai':
                player = AIPlayer(name)
            else:
                raise ValueError("Invalid player type. Please enter 'human' or 'ai'.")
            self.players.append(player)
        self.deck = [Card(rank, suit) for rank in range(1, 14) for suit in ['C', 'D', 'H', 'S']]
        random.shuffle(self.deck)
        self.winner = None  # Initialize winner attribute

    def play(self):
        player_scores = {}
        for player in self.players:
            score = self.play_hand(player)
            player_scores[player.name] = score
            print(f"{player.name}'s score: {score}")
        self.winner = max(player_scores, key=player_scores.get)
        print(f"The winner is {self.winner} with a score of {player_scores[self.winner]}.")

    def play_hand(self, player):
        hand = []
        while True:
            card = self.deck.pop()
            print(f"{player.name} drew: {card}")
            hand.append(card)
            total = sum(min(card.rank, 10) for card in hand)  # Ace is 1 or 11, face cards are 10
            if total >= 21:
                if total == 21:
                    print(f"{player.name} reached 21!")
                else:
                    print(f"{player.name} busted!")
                return total
            if isinstance(player, HumanPlayer):
                choice = input("Do you want another card? (yes/no): ").lower()
                if choice != 'yes':
                    break
            elif isinstance(player, AIPlayer):
                if total < 17:
                    print(f"{player.name} wants another card.")
                else:
                    print(f"{player.name} stands.")
                    break
        return total

if __name__ == "__main__":
    num_players = int(input("Enter number of players: "))
    game = BlackJackGame(num_players)
    game.play()
