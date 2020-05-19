import functions

# Creates the chips
chips = functions.Chips()

# Game loop that allows as many rounds as the player wants
while True:
    # Deck is created and shuffled
    print('Welcome to BlackJack!')
    deck = functions.Deck()
    deck.shuffle()
    
    # Asks the player to bet
    functions.take_bet(chips)
    
    # Each players' hand is created and dealt 2 cards
    player = functions.Hand()
    dealer = functions.Hand()
    functions.hit(deck, player)
    functions.hit(deck, dealer)
    functions.hit(deck, player)
    functions.hit(deck, dealer)
    
    # Shows one of the dealer's cards, and  both of the player's
    functions.show_some(player, dealer)
    
    # Asks the player if he wants another card, loops as long as the player wants more cards
    while functions.playing:
        functions.hit_or_stand(deck, player)
        # stops the game and shows the cards if the player busted
        if functions.bust(player):
            functions.show_all(player, dealer)
            functions.dealer_wins(chips)
            break
        # shows the cards after each new card drawn
        else:
            functions.show_some(player, dealer)
    # Dealer draws until he has equal or more points than the player
    while dealer.value <= player.value:
        if dealer.value < 21:
            functions.hit(deck, dealer)
            
    # Shows all the cards
    functions.show_all(player, dealer)
    
    # Decides the game winner
    if functions.bust(dealer):
        functions.player_wins(chips)
    elif player.value == dealer.value:
        functions.push()
        
    # Asks the player if he wants to continue playing
    if functions.replay(chips) == 'n':
        break
    else:
        functions.playing = True
