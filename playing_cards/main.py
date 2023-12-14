class Card:

    def __init__(self, suit, number, weight=None):
        self.suit = suit
        self.number = number
        self.weight = weight or number

    def __add__(self, other):
        return self.weight + other.weight


one_card = Card('Bubna', 6)
second_card = Card('Chervi', 9)
print(one_card + second_card)
