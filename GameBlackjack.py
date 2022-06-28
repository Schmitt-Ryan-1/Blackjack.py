import random
# inport card class from Card.py
from Card import Card
from Player import Player

# This is where the game logic will happen.
# Deck is defined here.
class Game:
    def __init__(self, game_name):
        self.game_name = game_name

# Deck is defined here. Produces shuffled deck. Wondering why here and not in Card.py
    def create_deck(self):
        deck = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        names = ["2","3","4","5","6","7","8","9","10","J", "Q", "K", "A"]
        for suit in suits:
            for name in names:
                deck.append(Card(suit, name))
                random.shuffle(deck)
        return (deck)

# Main has everything that will be run... lots of while loops
# 1 - The dealer shuffles the deck producing a randomized list of cards. - Done. May go into main?
# 2 - The Deal - Dealer deals Deck[0] face up to player, Deck[1] face down to self, Deck[2] FU to player, Deck[3] FU to self.
# 3 - If player has blackjack(21) player wins.
# 4 - Dealer checks FD card if FU card is A or has value of 10. If Blackjack dealer wins.
# 5 - Player inputs hit or stay. Ace value will be assumed 11 unless that busts then Ace value will be 1. Dealer wins if count > 21.
# 6 - After players turn is over dealer reveals hidden card.
# 7 - The dealer will keep hitting if count < 17. Will stay if count >= 17 . Player wins if dealer busts.
# 8 - Whoever is closest to 21 without going over wins.
# 9 - Promp to play again.

#not sure about this print statement
def main():
    game = Game("blackjack")
    new_deck = game.create_deck()
    for card in new_deck:
        print(card.toString())

if __name__ == "__main__":
    main
    pass
