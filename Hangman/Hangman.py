import random

from hangman_imports import word_list, stages, logo

chosen_word = random.choice(word_list)
total_lives = 6
lives_remaining = total_lives
# This variabe: lives_remaining is unnecessary as the code can be run the same way with only using the total_lives variable.
game_over = False
correct_letters = []

print(f"Yo Yo Yo... let's play\n{logo}")

while not game_over:
    print(f"****************************{lives_remaining}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed: {guess}")
        
    display = ""
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display+= " _"
        
    print("Word to guess: " + display)
    
    if guess not in chosen_word:
        lives_remaining -= 1
        print(f"Your guess {guess}, is not in the word! You lose a life!")
        if lives_remaining == 0:
            game_over = True
            print(f"*********************** YOU LOST! The correct word was: {chosen_word} **********************")
    
    if "_" not in display:
        game_over = True
        print(f"*********************** YOU WON! The correct word was indeed: {chosen_word} **********************")
    print(stages[lives_remaining])