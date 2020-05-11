import functions

chips = functions.Chips()

while True:
    print('Welcome to BlackJack!')
    deck = functions.Deck()
    deck.shuffle()
    functions.take_bet(chips)

    player = functions.Hand()
    dealer = functions.Hand()
    functions.hit(deck, player)
    functions.hit(deck, dealer)
    functions.hit(deck, player)
    functions.hit(deck, dealer)

    functions.show_some(player, dealer)

    while functions.playing:
        functions.hit_or_stand(deck, player)
        if functions.bust(player):
            functions.show_all(player, dealer)
            functions.dealer_wins(chips)
            break
        else:
            functions.show_some(player, dealer)
    while dealer.value <= player.value:
        if dealer.value < 21:
            functions.hit(deck, dealer)
    functions.show_all(player, dealer)
    if functions.bust(dealer):
        functions.player_wins(chips)
    elif player.value == dealer.value:
        functions.push()
    if functions.replay(chips) == 'n':
        break
    else:
        functions.playing = True
