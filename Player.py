# Thinking of putting deal in main function and not in the dealer since it's a function of the game and a dealer doesn't have to deal.
# Wonderring if count, Blackjack, Dbl, Split, Stay, Hit, Bust, win lose can all go into main ad functions of the game not the player.
class Player:
    def __init__(self, player, dealer, count):
        self.player = player(player, count)
        self.dealer = dealer(dealer, count)
        self.cards = cards
        self.count = count

# created a "hand" as an empty list to hold cards. Could this be it's own class to help de clutter the player class ie is a cluttered class better than too many classes.
    def hand(self, cards, count):
        hand = [ ]

# this is where we deal cards into the empty hand lists []
# would like to use def.hidden function from Card.py but not sure how to link the two. Do I just say hand(player) = [True, True] hand(dealer)= [False, True]
# could this be a part of the hand function above?
    def add_card(self, card):
        if len(hand) < 2:
            # somehow add a card from Caed.py class to hand lists
        else:
            return hand

# Blackjack - Both
    def blackjack(self, player):
        if count == 21:
            return blackjack
            print("Blackjack Bitch!")
        else:
            return hand

# Stay - Both
# in main, have inputs to_upper(s) and to upper(H) for
    def hit_stay(count):
        if player_input = "S":
            return hand
        elif player_input = "H"
            # add one card crom Card.py to hand \
        else:
            print('Invalid input, please input "H" to hit or "S" to stay.')

# Bust - Both
    def bust(self):
        if count < 21:
            return count
        else:
            return bust
            print("You Busted Bitch!")

# Win - Both
    def win(self):
        if player_count > dealer_count:
            print("Player wins! Suck Dicks dealer!")

# Lose - Both
    def both(self):
        if player_count <= dealer_count:
            print("Deealer wins! You suck!")
