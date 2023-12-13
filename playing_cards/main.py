class Card:

    def __init__(self, suit, number, weight=None):
        self.suit = suit
        self.number = number
        self.weight = weight if weight is not None else number


one_card = Card('Bubna', 6)

