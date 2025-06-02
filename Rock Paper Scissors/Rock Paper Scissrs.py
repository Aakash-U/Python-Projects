rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]
while True:
    your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

    if your_choice >0 and your_choice <= 2:
        print(game_images[your_choice])

    computer_choice = random.randint(a=0, b=2)

    print(f"Computer chose {game_images[computer_choice]}")

    if your_choice >= 3: print("Invalid input. You Lose!")
    elif your_choice == 0 and computer_choice == 2:
        print("You Win!")
    elif computer_choice > your_choice:
        print("You Lose!")
    elif your_choice == computer_choice:
        print("It's a draw!")
    elif your_choice == 2 and computer_choice == 0:
        print("You Lose!")
    elif your_choice > computer_choice:
        print("You Win!")