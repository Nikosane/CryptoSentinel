# Entry point for the program

def main():
    print("Welcome to CryptoSentinel")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    choice = input("Choose an option: ")
    if choice == "1":
        from encryption.encryptor import encrypt_file
        file_path = input("Enter the file path to encrypt: ")
        password = input("Enter the password: ")
        encrypt_file(file_path, password)
    elif choice == "2":
        from encryption.decryptor import decrypt_file
        file_path = input("Enter the file path to decrypt: ")
        password = input("Enter the password: ")
        decrypt_file(file_path, password)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()