import os
import random
from blackjack_imports import logo

def clear_console():
    os.system('clear')  # or 'cls' on Windows

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def adjust_for_ace(cards, score):
    while score > 21 and 11 in cards:
        cards[cards.index(11)] = 1
        score -= 10
    return score

def calculate_score(card_list):
    return adjust_for_ace(card_list, sum(card_list))

while True:
    play = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ")
    
    if play != 'y':
        print("Goodbye!")
        break

    clear_console()
    print("Welcome Player!\n")
    print(logo)

    players_cards = [random.choice(cards), random.choice(cards)]
    computers_cards = [random.choice(cards), random.choice(cards)]

    game_continues = True

    player_score = calculate_score(players_cards)
    computer_score = calculate_score(computers_cards)

    if player_score == 21 and len(players_cards) == 2 and computer_score == 21 and len(computers_cards) == 2:
        print("Both have Blackjack. It's a Draw!")
        continue
    elif player_score == 21 and len(players_cards) == 2:
        print("You Win! BlackJack")
        continue
    elif computer_score == 21 and len(computers_cards) == 2:
        print("You Lose! Dealer has BlackJack")
        continue

    print(f"Your Cards: {players_cards}, Current Score: {player_score}")
    print(f"Computer's First Card: {computers_cards[0]}")

    # --- PLAYER TURN ---
    while game_continues:
        another_card = input("Do you want another card? Press 'y' to hit and 'n' to stay: ")

        if another_card == "y":
            players_cards.append(random.choice(cards))
            player_score = calculate_score(players_cards)
            print(f"Your Cards: {players_cards}, Current Score: {player_score}")
            print(f"Computer's First Card: {computers_cards[0]}")
            if player_score > 21:
                print("You went over 21. You lose!")
                game_continues = False
        else:
            game_continues = False

    # --- COMPUTER TURN ---
    while computer_score < 17:
        computers_cards.append(random.choice(cards))
        computer_score = calculate_score(computers_cards)

    # --- Final Comparison ---
    if player_score <= 21:
        print(f"\nYour Final Hand: {players_cards}, Final Score: {player_score}")
        print(f"Computer's Final Hand: {computers_cards}, Final Score: {computer_score}")

        if computer_score > 21 or player_score > computer_score:
            print("You Win!")
        elif player_score == computer_score:
            print("It's a Draw!")
        else:
            print("Computer Wins!")