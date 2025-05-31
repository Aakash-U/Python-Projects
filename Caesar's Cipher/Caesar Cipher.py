from cipher_imports import logo, alphabet

def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            final_position = alphabet.index(letter) + shift
            final_position %= len(alphabet)
            cipher_text += alphabet[final_position]
        else:
            cipher_text += letter
    print(f"Here is your encoded message: {cipher_text}")     
    
def decrypt(text, shift):
    decipher_text = ""
    for letter in text:
        if letter in alphabet:
            initial_position = alphabet.index(letter) - shift
            initial_position %= len(alphabet)
            decipher_text += alphabet[initial_position]
        else:
            decipher_text += letter
    print(f"Here is your decoded message: {decipher_text}")

def caesar(direction, text, shift):
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)

print(logo)

run_again = "yes"
while run_again == "yes":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    caesar(direction, text, shift)

    run_again = input("Type 'yes' if you want to go again. Otherwise, type 'no':\n").lower()

print ("Bye!")