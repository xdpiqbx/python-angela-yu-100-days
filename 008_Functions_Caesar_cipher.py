from day_Caesar_art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_amount, cipher_direction):
    alphabet_len = len(alphabet)
    shift_amount %= alphabet_len
    result_message = ""
    for letter in plain_text:
        if letter.isalpha():
            if cipher_direction == 'E':
                index = alphabet.index(letter) + shift_amount
                if index > (alphabet_len - 1):
                    index -= alphabet_len
            else:
                index = alphabet.index(letter) - shift_amount
                if index < 0:
                    index += alphabet_len
            result_message += alphabet[index]
        else:
            result_message += letter
    print(cipher_direction)
    print(shift_amount)
    print(plain_text)
    print(result_message)
    return result_message


print(logo)

restart = "Y"

while restart == "Y":
    direction = input("Type 'E' to encrypt, type 'D' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'Y' if you want to go again. Otherwise type 'N'.")