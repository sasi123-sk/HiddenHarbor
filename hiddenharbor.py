import subprocess
import base64
import codecs
import re
from colorama import Fore, Style

def banner():
    print(Fore.GREEN + r'''
 _   _ _     _     _            _   _            _
| | | (_) __| | __| | ___ _ __ | | | | __ _ _ __| |__   ___  _ __
| |_| | |/ _` |/ _` |/ _ \ '_ \| |_| |/ _` | '__| '_ \ / _ \| '__|
|  _  | | (_| | (_| |  __/ | | |  _  | (_| | |  | |_) | (_) | |
|_| |_|_|\__,_|\__,_|\___|_| |_|_| |_|\__,_|_|  |_.__/ \___/|_|
                                         - sasikaran.surge.sh
                                         - insta: 0xwhitedevil
                                         - Author: Sasikaran
    ''' + Style.RESET_ALL)

def steganography_menu():
    while True:
        print("\nSteganography Menu:")
        print(Fore.YELLOW + "1. Stegcrack")
        print("2. Zsteg")
        print("3. Exiftool")
        print("4. Steghide")
        print("5. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            path = input("Enter the path to the image: ")
            word = input("Enter the wordlist path: ")
            subprocess.run(["stegcrack", path, word])

        elif choice == "2":
            path = input("Enter the path to the image: ")
            subprocess.run(["zsteg", path])

        elif choice == "3":
            path = input("Enter the path to the image: ")
            subprocess.run(["exiftool", path])

        elif choice == "4":
            path = input("Enter the path to the image: ")
            subprocess.run(["steghide", "extract", "-sf", path])

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def cipher_decoding_menu():
    while True:
        print("\nCipher Decoding Menu:")
        print(Fore.CYAN + "1. Caesar Cipher Decoder")
        print("2. Morse Code Decoder")
        print("3. XOR Cipher Decoder")
        print("4. General Cipher Decoder")
        print("5. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            cipher_text = input("Enter the Caesar cipher text: ")
            key = int(input("Enter the key: "))
            decrypted_text = caesar_cipher_decrypt(cipher_text, key)
            print("Decrypted Text:", decrypted_text)

        elif choice == "2":
            morse_code = input("Enter the Morse code: ")
            decoded_text = morse_code_decrypt(morse_code)
            print("Decrypted Text:", decoded_text)

        elif choice == "3":
            cipher_text = input("Enter the XOR cipher text in hexadecimal format: ")
            key = input("Enter the XOR key in hexadecimal format: ")
            decrypted_text = xor_cipher_decrypt(cipher_text, key)
            print("Decrypted Text:", decrypted_text)

        elif choice == "4":
            cipher_text = input("Enter the cipher text: ")
            decoded_text = general_cipher_decrypt(cipher_text)
            print("Decrypted Text:", decoded_text)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def caesar_cipher_decrypt(cipher_text, key):
    decrypted_text = ""
    for char in cipher_text:
        if char.isalpha():
            shifted_char = chr((ord(char) - key - ord('A')) % 26 + ord('A')) if char.isupper() else chr((ord(char) - key - ord('a')) % 26 + ord('a'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def morse_code_decrypt(morse_code):
    morse_dict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                  '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                  '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                  '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                  '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                  '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
                  '...--': '3', '....-': '4', '.....': '5', '-....': '6',
                  '--...': '7', '---..': '8', '----.': '9', '|': ' '}
    morse_words = morse_code.split(' ')
    decoded_text = ''.join([morse_dict[word] for word in morse_words])
    return decoded_text

def xor_cipher_decrypt(cipher_text, key):
    cipher_bytes = bytes.fromhex(cipher_text)
    key_bytes = bytes.fromhex(key)
    decrypted_bytes = bytes(x ^ y for x, y in zip(cipher_bytes, key_bytes))
    return decrypted_bytes.decode('utf-8')

def general_cipher_decrypt(cipher_text):
    # Add more cipher decoding methods here
    # Example: Base64 decoding
    try:
        decoded_text = base64.b64decode(cipher_text).decode('utf-8')
        return decoded_text
    except Exception as e:
        return f"Error decoding: {str(e)}"

def main():
    banner()
    while True:
        print("\nMain Menu:")
        print(Fore.MAGENTA + "1. Steganography Tools")
        print("2. Cipher Decoding Tools")
        print("3. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            steganography_menu()

        elif choice == "2":
            cipher_decoding_menu()

        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
