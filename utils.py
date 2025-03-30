import math
import random


def is_prime(n):
    """
    Check if a number is prime

    Args:
        n (int): Number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime(min_value=17, max_value=100):
    """
    Generate a prime number within a given range

    Args:
        min_value (int): Minimum value for prime number
        max_value (int): Maximum value for prime number

    Returns:
        int: A prime number within the specified range
    """
    while True:
        candidate = random.randint(min_value, max_value)
        if is_prime(candidate):
            return candidate


def find_primitive_root(p):
    """
    Find a primitive root modulo p

    Args:
        p (int): Prime number

    Returns:
        int: A primitive root modulo p
    """
    if p < 2:
        raise ValueError("p must be at least 2")

    def prime_factors(n):
        """
        Find prime factors of a number
        """
        factors = []
        d = 2
        while n > 1:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
            if d * d > n:
                if n > 1:
                    factors.append(n)
                break
        return list(set(factors))

    def is_primitive_root(g, p, factors):
        """
        Check if a number is a primitive root
        """
        for factor in factors:
            if pow(g, (p - 1) // factor, p) == 1:
                return False
        return True

    factors = prime_factors(p - 1)

    for g in range(2, p):
        if is_primitive_root(g, p, factors):
            return g

    raise ValueError(f"No primitive root found for {p}")