# core/text_encryption.py
from .encryption import HomomorphicEncryption


class TextHomomorphicEncryption:
    def __init__(self, p=17, g=3):
        """
        Initialize text homomorphic encryption

        Args:
            p (int): Prime number
            g (int): Generator for modular exponentiation
        """
        self.numeric_encryption = HomomorphicEncryption(p, g)

    def encrypt_text(self, text):
        """
        Encrypt text by converting to numeric values

        Args:
            text (str): Text to encrypt

        Returns:
            list: List of encrypted numeric values
        """
        # Convert text to numeric representation
        encrypted_chars = []
        for char in text:
            # Convert char to ASCII and encrypt
            numeric_val = ord(char)
            encrypted_char = self.numeric_encryption.encrypt(numeric_val)
            encrypted_chars.append(encrypted_char)

        return encrypted_chars

    def decrypt_text(self, encrypted_chars):
        """
        Decrypt text from encrypted numeric values

        Args:
            encrypted_chars (list): List of encrypted values

        Returns:
            str: Decrypted text
        """
        decrypted_text = ""
        for encrypted_char in encrypted_chars:
            # Decrypt numeric value and convert back to char
            numeric_val = self.numeric_encryption.decrypt(encrypted_char)
            decrypted_text += chr(numeric_val)

        return decrypted_text