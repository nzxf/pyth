
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
shift = int(input("Enter your code (1-27): "))
text = input("Enter your message: ")

def overflow(int):
    if int < -25:
        return (int * -1) % 25
    elif int < 0:
        return int * -1
    elif int <= 25:
        return int
    else:
        return int % 25


def cipher(direction,shift,text):
    # ENCODE = TURN SHIFT INTO NEGATIVE
    if direction == "decode":
        shift = shift * -1
    # START CHIPERING
    temp_text_list = []
    for element in text:
        # SEPARATE ALPHABET
        if element.isalpha():
            letter_index = overflow(alphabet.index(element.lower()) + shift)
            temp_text_list.append(alphabet[overflow(letter_index)])
        # SEPARATE SYMBOL & WHITESPACE
        else:
            temp_text_list.append(element)
    return "".join(temp_text_list)

print(cipher(direction,shift,text))

# def overflow (number):
#     if number >= 25:
#         return number%25
#     return number

# def cipher (letter):
#     if letter.isalpha():
#         current_letter_index = alphabet.index(letter.lower())
#         ciphered_letter = alphabet[overflow(current_letter_index + input_code)]
#         return ciphered_letter
#     else:
#         return letter

# def uncipher (letter):


# def phrase_cipher (phrase):
#     temporary_list = []
#     for letter in phrase:
#         temporary_list.append(cipher(letter))
#     return "".join(temporary_list)

# print(phrase_cipher(input_phrase))