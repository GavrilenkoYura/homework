class Card:

    def __init__(self, suit, number=None, weight=None):
        self.suit = suit
        self.number = number
        self.weight = weight or number

    def __add__(self, other):
        return self.weight + other.weight

    def __repr__(self):
        suits = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }
        return (f" _________\n|{str(self.number).ljust(8)}{suits[self.suit]}|\n|         |\n|"
                f"        |\n|{suits[self.suit]} {str(self.number).rjust(7)}|\n|_________|")


one_card = Card('Hearts', 6)
second_card = Card('Spades', 9)
print(one_card + second_card)
print(one_card)
