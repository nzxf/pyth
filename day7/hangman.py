import random
from database import words, hangman_stages

print("Welcom to Hangman!")

chosen_word = random.choice(words)
guess_word = []
for letter in chosen_word:
    guess_word.append("_")

gameover = False
tries = 0
current_guess_letter = "BLANK"

# while not gameover:
while gameover == False:
    guess_letter = input("Enter a letter! ").lower()
    
    # IF REENTER SAME INPUT (NO LOSING LIVES)
    if guess_letter == current_guess_letter or guess_letter in guess_word:
        print(f"You already guessed {guess_letter}")

    # IF MATCHED
    elif guess_letter in chosen_word:
        for letter in range(len(chosen_word)):
            if guess_letter == chosen_word[letter]:
                guess_word[letter] = guess_letter
    
    # IF NO MATCH
    else:
        tries += 1
       
    print(" ".join(guess_word).upper())
    print(hangman_stages[tries])

    # IF ALL GUESSED
    if "_" not in guess_word:
        gameover = True
        print("YOU WON!")

    # IF NO TRIES LEFT
    if tries >= 6:
        gameover = True
        print("YOU LOSE!")
        print(f"The answer is: {chosen_word.upper()}")

    current_guess_letter = guess_letter