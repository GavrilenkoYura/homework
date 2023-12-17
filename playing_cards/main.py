from random import choice


class Card:

    def __init__(self, suit: str, value, weight=None):
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

    @staticmethod
    def create_deck() -> list:
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        deck = []

        for _ in range(6):
            suit = choice(suits)
            value = choice(values)
            card = Card(suit, value)
            deck.append(card)

        return deck

    @staticmethod
    def sum_values(deck) -> int:
        return sum(card.weight for card in deck)

    @staticmethod
    def remove_card(deck, card):
        deck.remove(card)

    @staticmethod
    def shuffle_deck():
        new_deck = Card.create_deck()
        return new_deck

    @staticmethod
    def user_interaction():
        deck = Card.create_deck()
        print('Your deck:')
        print(*deck, sep='')

        while True:
            print('What would you like to do (sum/remove/shuffle/stop)')
            action = input().lower()

            match action:
                case 'sum':
                    print(f'The sum of the weights is: {Card.sum_values(deck)}')
                case 'remove':
                    print(f'Choose a card (enter a number from 1 to {len(deck)}: ')
                    card_index = int(input())
                    card = deck[card_index - 1]
                    Card.remove_card(deck, card)
                case 'shuffle':
                    deck = Card.shuffle_deck()
                case 'stop':
                    print('bye bye!')
                    break
                case _:
                    print('Invalid action. Try again.')

            print('Your deck:')
            print(*deck, sep='')


first_card = Card('Hearts', 'A', 11)
second_card = Card('Spades', 9)

Card.user_interaction()
