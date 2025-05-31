import random
import os

from blackjack_imports import logo

def clear_console():
    os.system('clear')

# Deal a single card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Calculate the score of a hand
def calculate_score(cards):
    # Check for Blackjack (Ace + 10 card)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Handle Aces (convert 11 to 1 if over 21)
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1

    return sum(cards)

# Compare final scores
def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, dealer has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Dealer went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# Main game function
def play_game():
    clear_console()
    print(logo)

    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    # Dealer draws until 17+
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())

    final_user_score = calculate_score(user_cards)
    final_dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {final_user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {final_dealer_score}")
    print(compare(final_user_score, final_dealer_score))

# Play loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()