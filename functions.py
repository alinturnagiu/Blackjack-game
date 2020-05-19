import random

# Dictionary defining the cards
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Variable used to keep asking the player if he wants another card
playing = True

# Creates the deck
class Deck:
    def __init__(self):
        self.deck = []
        for i in suits:
            for i2 in ranks:
                self.deck.append((i2, i))
          
    # Used to shuffle the cards
    def shuffle(self):
        random.shuffle(self.deck)
    
    # Used to take out a card from the deck to be given to a player
    def deal(self):
        return self.deck.pop()

# Class wich holds each of the players' cards
class Hand:
    def __init__(self):
        self.hand_cards = []
        self.value = 0
        self.aces = 0
          
    # Used to translate the cards' names from list to a normal readable names
    def __str__(self):
        s = ''
        for i in self.hand_cards:
            s += f' {i[0]} of {i[1]} |'
        return s
          
    # Adds a card to the hand, calculates the total points of the cards
    def add_card(self, card):
        self.hand_cards.append(card)
        self.value += values[card[0]]
        if card[0] == 'Ace':
            self.aces += 1

    # While there are Aces in hand and the total is > 21, it subtracts 10 points
    def adjust_ace(self):
        while self.value > 21 and self.aces != 0:
            self.value -= 10
            self.aces -= 1


# Class managing the game's currency          
class Chips:
    # Every game is started with 10 chips
    def __init__(self):
        self.total = 10
        self.bet = 0
          
    # Adds the bet amount to the bank
    def win_bet(self):
        self.total += self.bet

    # Subtracts the bet amount to the ban
    def lose_bet(self):
        self.total -= self.bet


# Takes the bet amount as an input, handles errors like input not an integer or betting more than owned
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(f'\nYou have {chips.total} chips\n'
                                  f'How many chips would you like to bet? \n> '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break

          
# Shows the player's hand but hides one of the dealer's cards
def show_some(player, dealer):
    x = str(dealer)
    print(f"\n\nDealer hand(??):\n<?????>{x[x.find('|'):]}\n")
    print(f'Player hand({player.value}):\n{str(player)}')

          
# Shows both players' hands
def show_all(player, dealer):
    print(f'\n\nDealer hand({dealer.value}):\n{str(dealer)}\n')
    print(f'Player hand({player.value}):\n{str(player)}')

          
# Takes a card from the deck and gives it to one of the players
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_ace()

          
# Keeps giving the player cards as long as he wants. Error handling to be added
def hit_or_stand(deck, hand):
    global playing
    a = input('Hit or stand?(h/s) > ').lower()
    if a == 'h':
        hit(deck, hand)
    else:
        playing = False

          
# Prints the winning message, gives the bet amount
def player_wins(chips):
    print("\nPlayer wins!")
    chips.win_bet()

          
# Prints the losing message, takes the bet amount
def dealer_wins(chips):
    print("\nDealer wins!")
    chips.lose_bet()

          
# Prints the draw message
def push():
    print("\nDealer and Player tie! It's a push.")

          
# Prints the bust message
def bust(hand):
    if hand.value > 21:
        return True

          
# Informs the player of the new amount of chips and asks if he wants to play again
def replay(chips):
    return input(f'\nYou have {chips.total} chips. Play again?(y/n) > ')
