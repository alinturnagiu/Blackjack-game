import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Deck:
    def __init__(self):
        self.deck = []
        for i in suits:
            for i2 in ranks:
                self.deck.append((i2, i))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.hand_cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        s = ''
        for i in self.hand_cards:
            s += f' {i[0]} of {i[1]} |'
        return s

    def add_card(self, card):
        self.hand_cards.append(card)
        self.value += values[card[0]]
        if card[0] == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        while self.value > 21 and self.aces != 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self):
        self.total = 10
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


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


def show_some(player, dealer):
    x = str(dealer)
    print(f"\n\nDealer hand(??):\n<?????>{x[x.find('|'):]}\n")
    print(f'Player hand({player.value}):\n{str(player)}')


def show_all(player, dealer):
    print(f'\n\nDealer hand({dealer.value}):\n{str(dealer)}\n')
    print(f'Player hand({player.value}):\n{str(player)}')


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_ace()


def hit_or_stand(deck, hand):
    global playing
    a = input('Hit or stand?(h/s) > ').lower()
    if a == 'h':
        hit(deck, hand)
    else:
        playing = False


def player_wins(chips):
    print("\nPlayer wins!")
    chips.win_bet()


def dealer_wins(chips):
    print("\nDealer wins!")
    chips.lose_bet()


def push():
    print("\nDealer and Player tie! It's a push.")


def bust(hand):
    if hand.value > 21:
        return True


def replay(chips):
    return input(f'\nYou have {chips.total} chips. Play again?(y/n) > ')
