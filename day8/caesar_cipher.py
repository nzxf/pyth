import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def overflow(int):
    # BUGGY
    if int < -25:
        return (int * -1) % 26
    elif int < 0:
        return int - 25
    # Work
    
    elif int <= 25:
        return int
    # BUGGY
    else:
        return int % 26


def cipher(direction,shift,text):
    # ENCODE = TURN SHIFT INTO NEGATIVE
    if direction == "decode":
        shift *= -1
    # START CHIPERING
    temp_text = ""
    for element in text:
        # SEPARATE ALPHABET
        if element.isalpha():
            letter_index = overflow(alphabet.index(element.lower()) + shift)
            temp_text += alphabet[overflow(letter_index)]
        # SEPARATE SYMBOL & WHITESPACE
        else:
            temp_text += element
    print("============================================")
    print(f"The {direction}d result: " + temp_text)
    print("============================================")

start_over = True
print(art.title)
while start_over:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
    shift = int(input("Enter your code: "))
    text = input("Enter your message: ")
    cipher(direction,shift,text)

    answer = input("Do you want to go again? 'yes' or 'no': ")
    if answer.lower() == "no":
        print(art.farewell)
        start_over = False
    elif answer.lower() == "yes":
        start_over = True