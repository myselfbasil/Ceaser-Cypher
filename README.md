# Caesar Cipher Encryption and Decryption

## Overview

The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher where each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet. This repository contains a Python implementation of the Caesar cipher for both encryption and decryption.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Features

- Simple command-line interface for user interaction.
- Ability to encrypt and decrypt text using a specified shift distance.
- Handles lowercase letters and wraps around the alphabet.
- Easy to understand and modify for educational purposes.

## How It Works

The Caesar cipher works by shifting each letter in the input text by a fixed number of positions in the alphabet. For example, with a shift of 3, 'a' becomes 'd', 'b' becomes 'e', and so on. If the shift moves past 'z', it wraps around to the beginning of the alphabet.

### Encryption

1. For each character in the input text, convert it to its ASCII value using `ord()`.
2. Add the specified shift distance to the ASCII value.
3. If the new ASCII value exceeds that of 'z', wrap around to 'a'.
4. Convert the new ASCII value back to a character using `chr()` and append it to the result.

### Decryption

The decryption process is similar but involves subtracting the shift distance instead of adding it. If the result goes below 'a', it wraps around to 'z'.

## Usage

To use the Caesar cipher program, follow these steps:

1. **Run the Program**: Execute the Python script in your terminal or command prompt.
   ```bash
   python caesar_cipher.py

2. **Choose an Option**: The program will present a menu with three options:
   - Encrypt
   - Decrypt
   - Exit

3. **Input Text**: Depending on your choice, you will be prompted to enter the text you want to encrypt or decrypt.

4. **Specify Shift Distance**: Enter the distance by which you want to shift the letters.

5. **View Results**: The program will display the encrypted or decrypted text and redirect you back to the main menu.

## Code Explanation

The code consists of two main functions, `encrypt` and `decrypt`, along with a user interface loop.

### Functions

- **`encrypt(user_input, distance)`**: 
  - Takes a string (`user_input`) and an integer (`distance`).
  - Iterates through each character, shifts it according to the distance, and handles wrapping around the alphabet.
  - Returns the encrypted string.

- **`decrypt(user_input, distance)`**: 
  - Similar to the `encrypt` function but subtracts the distance instead.
  - Handles wrapping for characters that go below 'a'.
  - Returns the decrypted string.

### Main Loop

The program runs in a loop, allowing the user to choose between encryption, decryption, or exiting the program. It validates user input and provides feedback for invalid choices.

## Example

### Encryption Example

```plaintext
Input: "hello"
Distance: 3
Output: "khoor"
```

### Decryption Example

```plaintext
Input: "khoor"
Distance: 3
Output: "hello"
```

## Limitations

- The current implementation only supports lowercase letters ('a' to 'z'). Uppercase letters and non-alphabetic characters are not handled.
- The program does not include error handling for non-integer distance inputs.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request. Please ensure that your code follows the existing style and includes relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the classic Caesar cipher algorithm.
- Thanks to the open-source community for their contributions and resources.
