from cryptography.fernet import Fernet

def decrypt_file(file_path, password):
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()

        key = Fernet.generate_key()
        cipher = Fernet(key)
        decrypted_data = cipher.decrypt(encrypted_data)

        output_file = file_path.replace('.enc', '_decrypted')
        with open(output_file, 'wb') as f:
            f.write(decrypted_data)

        print(f"File decrypted successfully: {output_file}")
    except Exception as e:
        print(f"Error decrypting file: {e}")
