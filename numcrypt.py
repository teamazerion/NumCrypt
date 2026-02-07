# NumCrypt v1.1
# Team Azerion - Secret Numeric Language Tool
# Commander: Jon Snow

import sys
import time
import os

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz0123456789.,!?@#"
SECRET_KEY = 7  # your private key

# Create mappings
char_to_num = {ALPHABET[i]: i+1 for i in range(len(ALPHABET))}
num_to_char = {i+1: ALPHABET[i] for i in range(len(ALPHABET))}

def clear():
    os.system("clear")

def banner():
    clear()
    print("""
 ███╗   ██╗██╗   ██╗███╗   ███╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗
 ████╗  ██║██║   ██║████╗ ████║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝
 ██╔██╗ ██║██║   ██║██╔████╔██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   
 ██║╚██╗██║██║   ██║██║╚██╔╝██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   
 ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║╚██████╗██║  ██║   ██║   ██║        ██║   
 ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   

                TEAM AZERION
        Commander: Jon Snow
    Secret Numeric Language Engine
    """)
    time.sleep(1)
    print(">>> FEDERAL CYBER SECURITY NOTICE <<<")
    print("This system is protected. Unauthorized decoding is prohibited.")
    print("All activities may be monitored.\n")
    time.sleep(1)

def encode(text):
    result = []
    for char in text:
        if char in char_to_num:
            num = char_to_num[char]
            encrypted = (num * SECRET_KEY) + 3
            result.append(str(encrypted))
    return " ".join(result)

def decode(code):
    result = []
    parts = code.split()
    for part in parts:
        try:
            num = int(part)
            decrypted = (num - 3) // SECRET_KEY
            if decrypted in num_to_char:
                result.append(num_to_char[decrypted])
        except:
            pass
    return "".join(result)

def menu():
    print("\n=== NumCrypt Control Panel ===")
    print("1. Encode text")
    print("2. Decode numbers")
    print("3. Exit")

# Start Program
banner()

while True:
    menu()
    choice = input("\nNumCrypt> ")

    if choice == "1":
        text = input("Enter text: ")
        encoded = encode(text)
        print("\n[ENCRYPTED CODE]")
        print(encoded)

    elif choice == "2":
        code = input("Enter code: ")
        decoded = decode(code)
        print("\n[DECRYPTED TEXT]")
        print(decoded)

    elif choice == "3":
        print("\nShutting down NumCrypt...")
        print("Team Azerion signing off.")
        sys.exit()

    else:
        print("Invalid command")
