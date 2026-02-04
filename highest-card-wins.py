# Name: Abigail Bui
# Period: 7
# Assignment: Week 4 HW - High Card Wins
# Time Spent: like 3 hours 

import random

# the deck of cards
deck = ['2 of ♠', '3 of ♠', '4 of ♠', '5 of ♠', '6 of ♠', '7 of ♠', '8 of ♠', '9 of ♠', '10 of ♠', 'a Jack of ♠', 'a Queen of ♠', 'the King of ♠', '♠A', 
        '2 of ♥', '3 of ♥', '4 of ♥', '5 of ♥', '6 of ♥', '7 of ♥', '8 of ♥', '9 of ♥', '10 of ♥', 'a Jack of ♥', 'a Queen of ♥', 'the King of ♥', '♥A', 
        '2 of ♣', '3 of ♣', '4 of ♣', '5 of ♣', '6 of ♣', '7 of ♣', '8 of ♣', '9 of ♣', '10 of ♣', 'a Jack of ♣', 'a Queen of ♣', 'the King of ♣', '♣A', 
        '2 of ♦', '3 of ♦', '4 of ♦', '5 of ♦', '6 of ♦', '7 of ♦', '8 of ♦', '9 of ♦', '10 of ♦', 'a Jack of ♦', 'a Queen of ♦', 'the King of ♦', '♦A']

play = input('Would you like to play? (Yes or no): ') # asks if user wants to play; if yes code below executes

if play == 'yes' or play == 'YES' or play == 'Yes': 
    # rule before starting
    print("Rules of the Game: You will be dealt 5 cards. You may exchange up to 3 of these cards if you please. After you are satisfied with your 5 cards, or you have run out of exchanges, you must pick one of these 5 cards. The rest will be discarded. After you pick your card, the program, will draw a card for itself. If your chosen card is higher than the program's card you win!")

    # drawing 5 cards
    draw = input('Enter D to draw: ')

    if draw == 'D':
        # assigns variable value for the # of loops to be executed below
        dealt = 5
        # empty list to add the dealt cards to
        five_cards = []

        while dealt > 0: # loops 5 times to get 5 cards
            # randomly chooses a card from the deck
            card = random.choice(deck)
            # adds the randomly chosen card to the empty list for the cards the player draws
            five_cards.append(card)
            # removes the randomly chosen card from the larger deck
            deck.remove(card)
            # subtracts from 'dealt' variable so the loop ends after 5 times
            dealt -= 1

        # prints the 5 cards the player was dealt so the player can see
        print(five_cards)

        # assigns variable value for the # of loops to be executed below
        chances = 3
        
        while chances > 0: # loops three times so player has a max of 3 times 
            # asks if user wants to replace a card
            change = input('Would you like to exhange one of these cards for a replacement? ')

            # if player does want to exchange a card then..
            if change == 'Yes' or change == 'YES' or change =='yes':
                # code will ask which card they want to swap out
                three_cards = int(input('What card would you like to swap? (1, 2, 3, 4, or 5): '))
                # code will swap the chosen card with a random choice from the deck
                five_cards[three_cards-1] = random.choice(deck)
                # removes the new card from the deck
                deck.remove(five_cards[three_cards-1])
                # prints the new five cards to show the player
                print(five_cards)
                # subtracts 1 to eventually end the loop
                chances -= 1
            else:
                # if the player says anything besides yes, the while loop will end
                chances = 0
                # user chooses one of the cards from the final 5 cards they have
                choosing = int(input('Pick your final card (1, 2, 3, 4, or 5): '))
                # takes player's choice from the list of the 5 cards
                your_card = (five_cards[choosing-1])
                # shows player their chosen card
                print(f"Your card is: {your_card}")
                # randomly chooses a card from the now smaller deck for the program
                program_card = random.choice(deck)
                # shows the player the program's card
                print (f"The program drew the card: {program_card}")
                # compares the program's card and the player's card
                if program_card > your_card: 
                    # if the program's card is higher than the player's the player loses
                    print('You lose. Better luck next time.')
                else:
                    # if the program's card is not higher than the player's card the player wins
                    print('Congrats! You win!')

# i had to play around with the wordings of the cards so they'd be compared correctly
# interestingly enough, the code does break ties using suit order, just a different suit order than commonly used
# i think spades was the lowest, followed by cloves, followed by hearts, with diamonds as the highest when i was testing it
# not sure why but its interesting (it's almost the suit order that i use for the card game 13, except in that game hearts is the highest)

