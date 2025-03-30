# core/encryption.py
import random


class HomomorphicEncryption:
    def __init__(self, p=17, g=3):
        """
        Initialize homomorphic encryption with prime and generator

        Args:
            p (int): Prime number
            g (int): Generator for modular exponentiation
        """
        self.p = p  # Prime number
        self.g = g  # Generator
        self.private_key = None  # Will be set during key generation

    def generate_key(self, private_key=None):
        """
        Generate a private key if not provided

        Args:
            private_key (int, optional): Custom private key. If None, randomly chosen.

        Returns:
            tuple: Public and private keys
        """
        if private_key is None:
            private_key = random.randint(1, self.p - 1)

        self.private_key = private_key

        # Public key is g^private_key mod p
        public_key = pow(self.g, private_key, self.p)

        return public_key, private_key

    def encrypt(self, message):
        """
        Encrypt a numeric message

        Args:
            message (int): Message to encrypt

        Returns:
            tuple: Encrypted message (ciphertext)
        """
        if self.private_key is None:
            self.generate_key()

        # Random ephemeral key
        r = random.randint(1, self.p - 1)

        # Encryption: (g^r mod p, m * public_key^r mod p)
        c1 = pow(self.g, r, self.p)
        public_key = pow(self.g, self.private_key, self.p)
        c2 = (message * pow(public_key, r, self.p)) % self.p

        return (c1, c2)

    def decrypt(self, ciphertext):
        """
        Decrypt a ciphertext

        Args:
            ciphertext (tuple): Encrypted message

        Returns:
            int: Decrypted message
        """
        if self.private_key is None:
            raise ValueError("Private key not set. Generate keys first.")

        c1, c2 = ciphertext

        # Decryption: m = c2 / (c1^private_key)
        s = pow(c1, self.private_key, self.p)
        s_inv = pow(s, self.p - 2, self.p)  # Modular multiplicative inverse

        message = (c2 * s_inv) % self.p

        return message

    def homomorphic_add(self, ciphertext1, ciphertext2):
        """
        Perform homomorphic addition

        Args:
            ciphertext1 (tuple): First encrypted message
            ciphertext2 (tuple): Second encrypted message

        Returns:
            tuple: Encrypted sum
        """
        c1_1, c2_1 = ciphertext1
        c1_2, c2_2 = ciphertext2

        # Homomorphic addition: multiply c1 and c2 components
        c1_result = (c1_1 * c1_2) % self.p
        c2_result = (c2_1 * c2_2) % self.p

        return (c1_result, c2_result)

    def homomorphic_multiply(self, ciphertext1, ciphertext2):
        """
        Perform homomorphic multiplication

        Args:
            ciphertext1 (tuple): First encrypted message
            ciphertext2 (tuple): Second encrypted message

        Returns:
            tuple: Encrypted product
        """
        c1_1, c2_1 = ciphertext1
        c1_2, c2_2 = ciphertext2

        # Homomorphic multiplication: perform specific operations
        c1_result = (c1_1 * c1_2) % self.p
        c2_result = (c2_1 * c2_2) % self.p

        return (c1_result, c2_result)