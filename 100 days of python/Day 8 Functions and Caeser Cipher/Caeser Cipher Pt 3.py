#Part 3 is combining everything to make the code more organized

alphabet = [" ", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(plain_text, shift_amount,cipher_direction):
    cipher_text = ""
    if direction == "decode":
        #similar to new_position = position - shift_amount. However basically takes the number and multiples by -1 in order to reverse. 
        shift_amount *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher_text += alphabet[new_position]
    print(cipher_text)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

caeser(plain_text=text,shift_amount=shift,cipher_direction=direction)