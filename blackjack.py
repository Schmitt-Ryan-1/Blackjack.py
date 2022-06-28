import random

Ok... So... So far I have a very rough outline and am struggling on how to start and how to tackle something this big.

OBJECT- the object of blackjack is to beat the dealer by getting a score as close to 21 without going over.

First i'm going to just try and make the game work and then I will worry about the gambling portion.
I don't know if i should bother with things like insurance right away but i think i should include splitting and doubling down, just not the betting aspects of those.

What I think the flow of the program will look like...

Set up the classes (so far I have six, I don't know if i need the cards or if they can just be included in the deck)... Player, Dealer, Cards, Deck, Hands, Game logic

    -Player- Attributes(Cards(function for count based on cards), $)        Methods(Bet, Count, Hit, Stay, DBL Down, Split, Insurance, Win, Lose, Bust)
    -Dealer - Attributes(Cards, Count)      Methods(Shuffle, Deal, count, Hit, Stay, Win, Lose, Bust, Pay, Collect)\
    -Deck - Attributes(52 Cards, Order)        Methods(Shuffle, Be delt, Hit(one card from deck to dealer ))
    -Cards (not sure if this is needed or if Deck class will suffice) - Attributes (Suit, Rank, Value)      Methods(Be shuffled, Be delt, Be hit)
    -Hands - Attributes( Cards, Values)     Methods (Be delt, Count, Hit, Stay, Bust, Split)
    -Game Logic - This inclued deverything about how the game works. Not sure what atributes / methods are but includes list below

1 - The dealer shuffles the deck producing a randomized list of cards .
2 - Player places Bet.
3 - The Deal - Dealer deals Deck[0] face up to player, Deck[1] face down to self, Deck[2] FU to player, Deck[3] FU to self.
4 - If player has blackjack(21) player wins 1.5x bet.
5 - Player chooses to purchase insurance or not.
6 - Dealer checks FD card if FU card is A or has value of 10. If Blackjack dealer wins, Insurance paid . If not play continues, Insurance collected.
7 - Player inputs hit or stay. Ace value will be assumed 11 unless that busts then Ace value will be 1. Dealer wins if count > 21.
8 - After players turn is over dealer reveals hidden card.
9 - The dealer will keep hitting if count < 17. Will stay if 17 or higher. Player wins if dealer busts.
10 - Whoever is closest to 21 without going over wins.
11 - Bet is collected or paid by Dealer.
12 - Promp to play again.
