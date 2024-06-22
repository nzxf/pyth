import random

print("Welcom to Hangman!")

words = ["stand", "sleep", "work", "sit", "pen", "run"]
chosen_word = random.choice(words)
guess_word = []
for letter in chosen_word:
    guess_word.append("_")

gameover = False
tries = 5

while gameover == False:
    user_letter = input("Enter a letter! ")
    
    if user_letter in chosen_word:
        for letter in range(len(chosen_word)):
            if user_letter == chosen_word[letter]:
                guess_word[letter] = user_letter
        
    else:
        tries -= 1
        if tries <= 0:
            gameover = True
       
    print("".join(guess_word))
    print(f"Tries left: {tries}")

    if chosen_word == "".join(guess_word):
        gameover = True
        print("YOU WON!")
    elif tries <= 0:
        gameover = True
        print("YOU LOSE!")
