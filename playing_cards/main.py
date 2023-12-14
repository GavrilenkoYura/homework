class Card:

    def __init__(self, suit, value, weight=None):
        self.suit = suit
        self.value = value
        if value in ['J', 'Q', 'K']:
            self.weight = 10
        elif value == 'A':
            self.weight = weight or 1
        else:
            self.weight = weight or value

    def __add__(self, other):
        return self.weight + other.weight

    def __repr__(self):
        suits = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }
        return (f" __________\n|{str(self.value).ljust(8)}{suits[self.suit]}|\n|         |\n|"
                f"         |\n|{suits[self.suit]} {str(self.value).rjust(7)}|\n __________\n")


one_card = Card('Hearts', 'A')
second_card = Card('Spades', 9)
print(one_card + second_card)
print(one_card)
