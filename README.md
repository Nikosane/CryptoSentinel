# CryptoSentinel

Secure File Encryption is a Python-based project designed to provide robust file encryption and decryption using the Advanced Encryption Standard (AES). It enables users to securely protect sensitive files with password-based encryption, ensuring data confidentiality and integrity.

---

## Features

- **AES Encryption**: Implements strong symmetric encryption using the AES algorithm.
- **Password-Based Security**: Utilizes a password to derive encryption keys for added protection.
- **Cross-Platform**: Works on any system with Python installed.
- **User-Friendly Interface**: Simple command-line interface for encrypting and decrypting files.
- **Extensible**: Modular codebase for future enhancements.

---

## Prerequisites

Ensure you have the following:

- Python 3.8 or higher
- `cryptography` library installed

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cryptosentinel.git
   cd secure-file-encryption
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Encrypt a File

1. Run the program:
   ```bash
   python main.py
   ```
2. Choose the option to encrypt a file (option `1`).
3. Enter the path of the file you want to encrypt.
4. Provide a password for encryption.
5. The encrypted file will be saved with a `.enc` extension in the same directory.

### Decrypt a File

1. Run the program:
   ```bash
   python main.py
   ```
2. Choose the option to decrypt a file (option `2`).
3. Enter the path of the encrypted file (e.g., `file.txt.enc`).
4. Provide the password used for encryption.
5. The decrypted file will be saved with `_decrypted` appended to its name in the same directory.

---

## Examples

### Example File Encryption

Input File: `example.txt`

```
This is a test file containing sensitive information.
```

Command:

```bash
python main.py
```

Output File: `example.txt.enc` (binary format)

### Example File Decryption

Encrypted File: `example.txt.enc`

Command:

```bash
python main.py
```

Output File: `example_decrypted.txt`

```
This is a test file containing sensitive information.
```

---

## Future Enhancements

- Add a graphical user interface (GUI) using `tkinter` or `PyQt`.
- Support for batch file encryption and decryption.
- Enhanced error handling for invalid inputs.
- Integration with cloud storage solutions.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature name"
   ```
4. Push to your fork:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request to the main repository.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Cryptography Library](https://cryptography.io/) for providing robust encryption tools.
- Open-source contributors and community for their support.
