logo = '''
___________                                                   .___       .__                     .___
\__    ___/______   ____ _____    ________ _________   ____   |   | _____|  | _____    ____    __| _/
  |    |  \_  __ \_/ __ \\__  \  /  ___/  |  \_  __ \_/ __ \  |   |/  ___/  | \__  \  /    \  / __ | 
  |    |   |  | \/\  ___/ / __ \_\___ \|  |  /|  | \/\  ___/  |   |\___ \|  |__/ __ \|   |  \/ /_/ | 
  |____|   |__|    \___  >____  /____  >____/ |__|    \___  > |___/____  >____(____  /___|  /\____ | 
                       \/     \/     \/                   \/           \/          \/     \/      \/ 

'''
greet = "Welcome to Treasure Island. Your mission is to find the treasure."

print(logo)
print(greet)

typo = "You mistype. The Typo Police comes and arrests your. GAME OVER!"

step_1 = input("You are arrived on a mysterious island at night on a shattered boat. Where are you goind to go? Left or Right? ")

if step_1.lower() == "left":
    step_2 = input("There is dark jungle in front of you. Go inside the jungle without light or go back to your boat to take the torch? jungle or boat? ")
    if step_2 == "jungle":
        step_3 = input("You arrived at an open field and find three different dirt roads. One leads to a cave, another leads into a lake, and the last one goes up into a mountain. Cave, lake, or mountain? ")
        if step_3.lower() == "cave":
            print("You found a treasure chest filled with gold coins. YOU WON!")
            print('''
        *******************************************************************************
                |                   |                  |                     |
        _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     `"=.|                  |
        |___________________|__"=._o`"-._        `"=.______________|___________________
                |                `"=._o`"=._      _`"=._                     |
        _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
        _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
        |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
        |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/[TomekK]
        *******************************************************************************
        ''') 
        elif step_3.lower() == "lake":
            print("You arrived at the side of the lake. All of sudden a boar come running and attacked you with its huge tusks. GAME OVER!")
        elif step_3.lower() == "mountain":
            print("After 2 hours of climbing. You heard a burst of wind from above. A huge bird take you with its enormous talon, fly into the air, then drop you. GAME OVER!")
        else:
            print(typo)
    elif step_2 == "boat":
        print("While you searching for the torch, a giant octopus wraps its tentacles around the boat and crush you inside. GAME OVER!")
    else:
        print(typo)
elif step_1.lower() == "right":
    print("A crab as big as a house come running sideway toward you. You right leg got caught in between rocks then it snaps your body into two pieces. GAME OVER!")
else:
    print(typo)
