# Name: Abigail Bui
# Period: 7
# Assignment: Week 4 HW - High Card Wins
# Time Spent: 

import random

deck = [('♠', 2), ('♠', 3), ('♠', 4), ('♠', 5), ('♠', 6), ('♠', 7), ('♠', 8), ('♠', 9), ('♠', 10), ('♠', 'J'), ('♠', 'Q'), ('♠', 'K'), ('♠', 'A'), 
        ('♥', 2), ('♥', 3), ('♥', 4), ('♥', 5), ('♥', 6), ('♥', 7), ('♥', 8), ('♥', 9), ('♥', 10), ('♥', 'J'), ('♥', 'Q'), ('♥', 'K'), ('♥', 'A'), 
        ('♣', 2), ('♣', 3), ('♣', 4), ('♣', 5), ('♣', 6), ('♣', 7), ('♣', 8), ('♣', 9), ('♣', 10), ('♣', 'J'), ('♣', 'Q'), ('♣', 'K'), ('♣', 'A'), 
        ('♦', 2), ('♦', 3), ('♦', 4), ('♦', 5), ('♦', 6), ('♦', 7), ('♦', 8), ('♦', 9), ('♦', 10), ('♦', 'J'), ('♦', 'Q'), ('♦', 'K'), ('♦', 'A')]

play = input('Would you like to play? (Yes or no): ')

if play == 'yes' or play == 'YES' or play == 'Yes':
    print("Rules of the Game: You will get be dealt 5 cards. You must pick one of these 5 cards, the rest will be discarded. After you pick your card, the program, will draw a card for itself. If your chosen card is higher than the program's cardm you win!")
    draw = input('Enter D to draw: ')
    if draw == 'D':
        hand = [random.choices(deck, k=5)]
        print(hand)
        choosing = int(input('What card would you like to choose? (1, 2, 3, 4, or 5): '))
        your_choice = hand[choosing]
