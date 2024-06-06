import random
import rock_paper_scissor_art
choices = [rock_paper_scissor_art.rock, rock_paper_scissor_art.paper, rock_paper_scissor_art.scissor]

player_hand = int(input("What do you choos? Type 0 for Rock, 1 for Paper or 2 for Scissor. "))

computer_hand = random.randint(0, 2)

print(f"You chose:\n{choices[player_hand]}")
print(f"Computer chose:\n{choices[computer_hand]}")

if player_hand == computer_hand:
    print("IT'S A TIE")
elif player_hand == 0 and computer_hand == 2:
    print("YOU WON!!!")
elif player_hand == 1 and computer_hand == 0:
    print("YOU WON!!!")
elif player_hand == 2 and computer_hand == 1:
    print("YOU WON!!!")
else:
    print("YOU LOSE!!!")