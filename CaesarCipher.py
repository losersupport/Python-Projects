def encrypt_caesar_cipher(message, shift):
    encrypted_message = ""
    
    for char in message:
        if char.isalpha():  # Encrypt only alphabetic characters
            shift_amount = shift % 26  # Ensure shift stays within the alphabet range
            if char.islower():
                encrypted_message += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                encrypted_message += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_message += char  # Non-alphabet characters remain the same
    return encrypted_message

def decrypt_caesar_cipher(message, shift):
    return encrypt_caesar_cipher(message, -shift)

# Test the code with "cyber security"
message = "cyber security"
shift = 5  # Example shift

# Encrypt the message
encrypted_message = encrypt_caesar_cipher(message, shift)
print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message back
decrypted_message = decrypt_caesar_cipher(encrypted_message, shift)
print(f"Decrypted Message: {decrypted_message}")
