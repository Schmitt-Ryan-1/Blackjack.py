# create a card class. Represents ONE card.
# Thinking of a function defining an ace and how it can be 1 or 11 here
class Card:
    def __init__(self, suit, name, hidden):
    #link name to dictionary of card names with values
        self.suit = suit
        self.name = name
        self.hidden = hidden # maybe an atribute for the hidden dealer card ?

# Trying to think of a way to make A == 11 or 1 based on the score, maybe thisll work.
    def card_score(name):
        if rank == "A":
            return 11 or 1
        elif rank in ["k", "Q", "J"]:
             return 10
        else:
            return int(name)

# Trying to make an if else where the first dealer card is hidden. This may not work and may go elseware.
    def hidden.self():
        if hidden == True:
            return "[X]"
        else:
            return "[" + self.suit " of " + self.rank + "]"

# Turns card name, suit into string "x of x" example "A of Spades"
    def toString(self):
        return "{name} of {suit}".format(name = self.name, suit = self.suit)


# Create a dictionary to assign values to cards, replaced with card_score line 11
# Not sure about the A being 1 or 11.
    #card_value = {
        #'A': 1 or 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
    #}
