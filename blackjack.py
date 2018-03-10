#! python 3
import random


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]*4


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        hand.append(deck.pop())
    return hand


def is_blackjack(playerHand):
    return get_value(playerHand) == 21


def get_value(hand):
    value = 0
    acecount = 0
    for card in hand:
        if card == 11 or card == 12 or card == 13:
            value += 10
        elif card == 1:
            value += 11
            acecount += 1

        else:
            value += card
    if value > 21:
        value = value - acecount*10

    return value


def stand():
    pass


def hit(playerHand):
    card = deck.pop(0)
    playerHand.append(card)
    print(
        f'Card shown is {card}. Your hand now consists of {playerHand}'
        'with value of {get_value(playerHand)}')


print(f'Welcome to Blackjack')
playerHand = deal(deck)
dealerHand = deal(deck)


print(f'your hand is {playerHand}. Dealer is showing a {dealerHand[0]}')
if is_blackjack(playerHand):
    print('Congratulations. Player won with blackjack')

while True:
    choice = input('S to stand H to hit\n').upper()
    if choice == 'S':
        break
    if choice == 'H':
        hit(playerHand)
        if get_value(playerHand) > 21:
            print('You bust. Thank you for playing')
            break

print(playerHand)
