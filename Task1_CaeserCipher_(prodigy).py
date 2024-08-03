#IMPLEMENTING CAESER CIPHER IN PYTHON 

# Define constants for last character and character range. 
LAST_CHAR_CODE = ord('Z')
CHAR_RANGE = 26

#ENCRYPTION FUNCTION 

def encryption(Plain_text, shift):
    # Result placeholder
    result = ""
    # Go through each of the letters in the message
    for char in Plain_text.upper():
        if char.isalpha():
            # converting the characters to ASCII code
            char_code = ord(char)
            new_char_code = char_code + shift
            if new_char_code > LAST_CHAR_CODE:
                new_char_code -= CHAR_RANGE
            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char
    print(f"Encrypted text : {result}")
    
#DECRYPTION FUNCTION 

def decryption(Cipher_text, shift):
    result = ""
    for char in Cipher_text.upper():
        if char.isalpha():
            char_code = ord(char)
            new_char_code = char_code - shift
            if new_char_code < ord('A'):
                new_char_code += CHAR_RANGE
            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char
    print(f"Decrypted text : {result}")

Again = True
while Again:
    option = input(
        "For Encryption type (e) and for Decryption type (d): ").lower()
    if option not in ("d", "e"):
        print("invalid, Enter 'e' or 'd'.")
        continue
    shift = int(input("Enter Shift Value: "))
    message = input("Enter the message: ")
    if option == "e":
        encryption(message, shift)
    elif option == "d":
        decryption(message, shift)
    Repeat = input("Do you have more text?(y/n): ").lower()
    if Repeat != "y":
        Again = False
print("Program Ended")
