from auction_imports import logo, welcome, item_description
import os
def clear_console():
    os.system('clear')

print(logo)
print(welcome)
print(item_description)

auction_ended = False
bet = {}

while not auction_ended:
    bidder = input("Please enter your name: ")
    price = input("What is your bid amount? $ ")
    int_price = int(price)
    bet[bidder] = int_price
    new_bidder = input("Input 'Yes' if there are other bidders after you or 'No' if there aren't. ").lower()
    
    if new_bidder == 'yes':
        clear_console()
    elif new_bidder == 'no':
        auction_ended = True
        print("The auction has ended!")
        print("Thank you all for your participating!")

winner = ""
highest_bid = 0

for bidder in bet:
    if bet[bidder] > highest_bid:
        highest_bid = bet[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}. Congratulations {winner}, Pride of Manchester City #17 Kevin De Bruyne Jersey is yours!")