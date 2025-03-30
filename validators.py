import re


def validate_prime(p):
    """
    Validate if the input is a valid prime number

    Args:
        p (int or str): Prime number to validate

    Returns:
        bool: True if valid prime, False otherwise
    """
    try:
        p = int(p)
        if p < 2:
            return False

        # Basic primality test
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                return False
        return True
    except (ValueError, TypeError):
        return False


def validate_generator(g, p):
    """
    Validate if the generator is valid for the given prime

    Args:
        g (int or str): Generator to validate
        p (int): Prime number

    Returns:
        bool: True if valid generator, False otherwise
    """
    try:
        g = int(g)
        p = int(p)

        # Check basic constraints
        if g < 2 or g >= p:
            return False

        # Check if generator creates full multiplicative group
        powers = set()
        x = g
        for _ in range(p - 1):
            powers.add(x)
            x = (x * g) % p

        return len(powers) == p - 1
    except (ValueError, TypeError):
        return False


def validate_encryption_input(message, mode='numeric'):
    """
    Validate encryption input based on mode

    Args:
        message (str): Message to encrypt
        mode (str): Encryption mode ('numeric' or 'text')

    Returns:
        bool: True if input is valid, False otherwise
    """
    if mode == 'numeric':
        # Check if input is a valid integer
        try:
            int(message)
            return True
        except ValueError:
            return False

    elif mode == 'text':
        # Validate text input
        if not message:
            return False

        # Optional: Add more sophisticated text validation
        # For example, check for special characters or length
        return 1 <= len(message) <= 100

    else:
        raise ValueError(f"Unknown encryption mode: {mode}")
