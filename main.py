import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
reset = True

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position % len(alphabet)]
        else:
            end_text += char
        
    print(f"Here's the {cipher_direction}d result: {end_text}\n")

while reset:
    print(art.logo)
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    choice = input("Do you want to run this program. Type Yes or No.\n").lower()
    if choice == 'no':
        reset = False
        print("Thank you for using our program. Goodbye")