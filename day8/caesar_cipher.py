
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


input_code = int(input("Enter your code (1-27): "))
input_phrase = input("Enter your message: ")


def overflow (number):
    if number >= 26:
        return number%26
    return number

def cipher (letter):
    current_letter_index = alphabet.index(letter)
    ciphered_letter = alphabet[overflow(current_letter_index + input_code)]
    return ciphered_letter

def phrase_cipher (phrase):
    temporary_list = []
    for letter in phrase:
        temporary_list.append(cipher(letter))
    return "".join(temporary_list)

print(phrase_cipher(input_phrase))