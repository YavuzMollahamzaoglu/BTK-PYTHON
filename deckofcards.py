class Card:
    def __init__(self,suit,val):
        self.suit = suit
        self.val = val
    def show(self):
        print(f'{self.val} of {self.suit}')



class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    def build(self):
        for s in ['Spades', 'Clubs','Diamonds','Hearts']:
            for v in range(1,14):
                print(v)


