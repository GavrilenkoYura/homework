# Importing the choice function from the random module
from random import choice


# Defining the Card class
class Card:
    # Initializing the Card object
    def __init__(self, suit: str, value, weight=None):
        # Defining the suits
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        # Checking if the suit is valid
        if suit not in suits:
            raise ValueError("Invalid suit. It should be one of 'Hearts', 'Diamonds', 'Clubs', 'Spades'")
        self.suit = suit
        self.value = value
        # Assigning weights to the cards
        if value in ['J', 'Q', 'K']:
            self.weight = 10
        elif value == 'A':
            self.weight = weight or 1
        else:
            self.weight = weight or value

    # Representing the Card object
    def __repr__(self):
        # Defining the suits
        suits = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Clubs': '♣',
            'Spades': '♠'
        }
        # Returning the representation of the card
        return (f" _________ \n|{str(self.value).ljust(8)}{suits[self.suit]}|\n|         |\n|"
                f"         |\n|{suits[self.suit]} {str(self.value).rjust(7)}|\n _________ \n")

    # Creating a deck of cards
    @staticmethod
    def create_deck(num_cards=36) -> list:
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        deck = []

        for _ in range(num_cards):
            suit = choice(suits)
            value = choice(values)
            card = Card(suit, value)
            deck.append(card)

        return deck

    # Calculating the sum of the weights of the cards in the deck
    @staticmethod
    def sum_values(deck) -> int:
        return sum(card.weight for card in deck)

    # Removing a card from the deck
    @staticmethod
    def remove_card(deck, card):
        deck.remove(card)

    # Replacing the deck with a new one
    @staticmethod
    def replace_deck():
        new_deck = Card.create_deck()
        return new_deck

    # Interacting with the user
    @staticmethod
    def user_interaction():
        num_cards = int(input('Enter number of cards in the deck: '))
        deck = Card.create_deck(num_cards)
        print('Your deck:')
        print(*deck, sep='')

        while True:
            print('What would you like to do (sum/remove/replace/stop)')
            action = input().lower()

            match action:
                case 'sum':
                    print(f'The sum of the weights is: {Card.sum_values(deck)}')
                case 'remove':
                    print(f'Choose a card (enter a number from 1 to {len(deck)}: ')
                    card_index = int(input())
                    if card_index < 1 or card_index > len(deck):
                        print("Invalid card index. Try again.")
                        continue
                    card = deck[card_index - 1]
                    Card.remove_card(deck, card)
                case 'shuffle':
                    deck = Card.replace_deck()
                case 'stop':
                    print('bye bye!')
                    break
                case _:
                    print('Invalid action. Try again.')

            print('Your deck:')
            print(*deck, sep='')


# Creating two cards
first_card = Card('Hearts', 'A', 11)
second_card = Card('Spades', 9)

# Starting the user interaction
Card.user_interaction()
