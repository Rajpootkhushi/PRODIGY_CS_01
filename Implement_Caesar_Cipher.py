def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift % 26  

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            else: 
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char 
    return result

def main():
    mode = input("Choose mode (E)ncrypt or (D)ecrypt: ").strip().upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))

    if mode == 'E':
        print("Encrypted Message:", caesar_cipher(message, shift, 'encrypt'))
    elif mode == 'D':
        print("Decrypted Message:", caesar_cipher(message, shift, 'decrypt'))
    else:
        print("Invalid mode selected!")

if __name__ == "__main__":
    main()