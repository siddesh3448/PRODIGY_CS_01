"""
Caesar Cipher Cryptographic Engine
Author: Prodigy InfoTech Cyber Security Intern
Task: PRODIGY_CS_01 - Caesar Cipher Tool

Description:
    This module contains the core cryptographic logic for the Caesar Cipher.
    It provides functions to encrypt and decrypt text by shifting characters 
    along the English alphabet. All non-alphabetical characters (numbers, 
    spaces, punctuation, symbols) are preserved exactly as they are.

Educational Concepts Covered:
    1. Plaintext vs. Ciphertext: 
       - Plaintext is the readable message.
       - Ciphertext is the encrypted (scrambled) message.
    2. Shift Key (k): 
       - An integer representing how many positions each letter is moved.
    3. ord() Function:
       - Returns the Unicode/ASCII integer value of a character.
       - Example: ord('A') is 65, ord('a') is 97.
    4. chr() Function:
       - Returns the character corresponding to the ASCII integer.
       - Example: chr(65) is 'A', chr(97) is 'a'.
    5. Modular Arithmetic (% 26):
       - Ensures that if the shift goes beyond 'Z' or 'z', it wraps around 
         to the beginning of the alphabet ('A' or 'a').
"""

def encrypt(plaintext: str, shift: int) -> str:
    """
    Encrypts a plaintext string using the Caesar Cipher algorithm.
    
    Mathematical Formulation:
        E_k(x) = (x + k) mod 26
        Where:
            x = numerical index of plaintext letter (0 to 25)
            k = shift key
            E_k(x) = numerical index of ciphertext letter (0 to 25)
            
    Parameters:
        plaintext (str): The original message to encrypt.
        shift (int): The number of positions to shift each letter.
        
    Returns:
        str: The encrypted ciphertext message.
    """
    ciphertext_chars = []
    
    # Standardize the shift using modulo 26 to handle shifts greater than 26 or negative shifts
    effective_shift = shift % 26
    
    for char in plaintext:
        # Check if the character is an uppercase letter
        if char.isupper():
            # 1. Convert char to standard 0-25 range: ord(char) - ord('A')
            # 2. Apply shift: (ord(char) - ord('A') + effective_shift)
            # 3. Apply modulo 26 to wrap around: (...) % 26
            # 4. Map back to ASCII space: + ord('A')
            shifted_ascii = (ord(char) - ord('A') + effective_shift) % 26 + ord('A')
            ciphertext_chars.append(chr(shifted_ascii))
            
        # Check if the character is a lowercase letter
        elif char.islower():
            # 1. Convert char to standard 0-25 range: ord(char) - ord('a')
            # 2. Apply shift: (ord(char) - ord('a') + effective_shift)
            # 3. Apply modulo 26 to wrap around: (...) % 26
            # 4. Map back to ASCII space: + ord('a')
            shifted_ascii = (ord(char) - ord('a') + effective_shift) % 26 + ord('a')
            ciphertext_chars.append(chr(shifted_ascii))
            
        else:
            # If it's a number, space, or symbol, preserve it as is
            ciphertext_chars.append(char)
            
    return "".join(ciphertext_chars)


def decrypt(ciphertext: str, shift: int) -> str:
    """
    Decrypts a ciphertext string using the Caesar Cipher algorithm.
    
    Mathematical Formulation:
        D_k(x) = (x - k) mod 26
        Which is equivalent to shifting in the opposite direction: E_{-k}(x)
        
    Parameters:
        ciphertext (str): The encrypted message to decrypt.
        shift (int): The shift key that was originally used to encrypt the message.
        
    Returns:
        str: The decrypted plaintext message.
    """
    # Decryption is simply shifting in the negative direction.
    # Passing -shift to the encrypt function mathematically resolves the shift backwards:
    # (x - k) mod 26 == (x + (26 - k)) mod 26
    return encrypt(ciphertext, -shift)
