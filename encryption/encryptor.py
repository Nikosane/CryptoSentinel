from cryptography.fernet import Fernet
import os

def encrypt_file(file_path, password):
    try:
        key = Fernet.generate_key()
        cipher = Fernet(key)

        with open(file_path, 'rb') as f:
            data = f.read()

        encrypted_data = cipher.encrypt(data)

        with open(file_path + '.enc', 'wb') as f:
            f.write(encrypted_data)

        print(f"File encrypted successfully: {file_path}.enc")
    except Exception as e:
        print(f"Error encrypting file: {e}")
