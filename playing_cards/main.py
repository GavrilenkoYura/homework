from random import choice


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

    def __repr__(self):
        suits = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }
        return (f" _________ \n|{str(self.value).ljust(8)}{suits[self.suit]}|\n|         |\n|"
                f"         |\n|{suits[self.suit]} {str(self.value).rjust(7)}|\n _________ \n")


def add_cards(card1, card2):
    return card1.weight + card2.weight


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    deck = []

    for _ in range(6):
        suit = choice(suits)
        value = choice(values)
        card = Card(suit, value)
        deck.append(card)

    return deck


first_card = Card('Hearts', 'A', 11)
second_card = Card('Spades', 9)
result = add_cards(first_card, second_card)
print(result)

first_deck = create_deck()
print(*first_deck, sep='')
