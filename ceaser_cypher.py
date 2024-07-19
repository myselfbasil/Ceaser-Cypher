# Caesar cipher encryption
def encrypt(user_input, distance):
    code = ""
    for i in user_input:
        ciphervalue = ord(i) + distance
        if ciphervalue > ord('z'):
            ciphervalue=ciphervalue-ord('z')+ord('a')-1
        code += chr(ciphervalue)
    return code

# Caesar cipher decryption
def decrypt(user_input, distance):
    code = ""
    for i in user_input:
        ciphervalue = ord(i) - distance
        if ciphervalue < ord('a'):
            ciphervalue=ciphervalue+ord('z')-ord('a')+1
        code += chr(ciphervalue)
    return code
    
while True:
    print("------------------------- Main Menu -------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        user_input = input("Enter the text to encrypt: ")
        distance = int(input("Enter the specific distance variation:"))
        encrypted_text = encrypt(user_input,distance)
        print("Encrypted text:", encrypted_text)
        print("Redirecting you to the main menu!")
        
    elif choice == "2":
        user_input = input("Enter the text to decrypt: ")
        distance = int(input("Enter the specific distance variation:"))
        decrypted_text = decrypt(user_input,distance)
        print("Decrypted text:", decrypted_text)
        a=print("Do you want to return to the main menu?")
        print("Redirecting you to the main menu!")

    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
        
