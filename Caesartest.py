
# Task 1: Encrypt a Message
def caesar(plainText, shiftKey):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''  # Initialize an empty string for the result

    for char in plainText:
        if char.isalpha():  # Ensure the character is alphabetic
            char = char.lower()  # Work with lowercase for simplicity

            # Find the current index of the character in the alphabet
            current_index = alphabet.index(char)
            # Calculate the new shifted index (wrap around using modulo)
            shifted_index = (current_index + shiftKey) % 26
            # Append the shifted character
            new_char = alphabet[shifted_index]
            encrypted_text += new_char
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += char

    return encrypted_text


# Task 2: Decrypt a Message
def caesar_decrypt(cipherText, shiftKey):
    return caesar(cipherText, -shiftKey)


# Task 4: Custom Alphabet Encryption and Decryption
def caesar_encrypt_custom(plainText, shiftKey, alphabet):
    encrypted_text = ''  # Initialize an empty string for the result

    for char in plainText:
        if char.isalpha():  # Ensure the character is alphabetic
            is_upper = char.isupper()  # Check if the character is uppercase
            char = char.lower()  # Convert to lowercase for simplicity

            # Find the current index of the character in the custom alphabet
            current_index = alphabet.index(char)
            # Calculate the new shifted index (wrap around using modulo)
            shifted_index = (current_index + shiftKey) % len(alphabet)
            # Append the shifted character (convert back to uppercase if needed)
            new_char = alphabet[shifted_index]
            encrypted_text += new_char.upper() if is_upper else new_char
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_text += char

    return encrypted_text


def caesar_decrypt_custom(cipherText, shiftKey, alphabet):
    # Reuse the custom encryption function with a negative shift for decryption
    return caesar_encrypt_custom(cipherText, -shiftKey, alphabet)


# Task 5: Cracking the Caesar Cipher
def caesar_crack(cipher_text):
    possible_messages = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Use lowercase alphabet for consistency

    # Try every possible shift (0 through 25) to decrypt the message
    for shift in range(len(alphabet)):
        # Decrypt with the current shift and add the result to the list
        decrypted_message = caesar_decrypt(cipher_text, shift)
        possible_messages.append(f"Shift {shift}: {decrypted_message}")
    return possible_messages


# Main Execution Block
if __name__ == "__main__":
    # Example usage for Task 1 and Task 2
    plain_text = 'Hi my name is Elham 3'
    shift_key = 3

    # Encrypt the plaintext
    encrypted = caesar(plain_text, shift_key)
    print("Encrypted Text:", encrypted)

    # Decrypt the ciphertext
    decrypted = caesar_decrypt(encrypted, shift_key)
    print("Decrypted Text:", decrypted)

    # Task 4: Custom Alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    custom_alphabet = alphabet[::-1]  # Reversed alphabet

    # Encrypt the plaintext with the custom alphabet
    custom_encrypted = caesar_encrypt_custom(plain_text, shift_key, custom_alphabet)
    print("Custom Encrypted:", custom_encrypted)

    # Decrypt the ciphertext with the custom alphabet
    custom_decrypted = caesar_decrypt_custom(custom_encrypted, shift_key, custom_alphabet)
    print("Custom Decrypted:", custom_decrypted)

    # Task 5: Cracking the Caesar Cipher
    print("\nCracking the Caesar Cipher:")
    possible_decrypted = caesar_crack('Kl pb qdph lv Hohdp 3')  # Encrypted form of 'Hi my name is Elham'
    for message in possible_decrypted:
        print(message)





