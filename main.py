"""
Caesar Cipher Tool - Main Entry Point
Author: Prodigy InfoTech Cyber Security Intern
Task: PRODIGY_CS_01 - Caesar Cipher Tool

Description:
    This script provides a highly interactive, robust, and visually appealing 
    command-line interface (CLI) for the Caesar Cipher Encryption and Decryption Tool.
    
    It handles:
    - User input validation (for menu choices and shift values).
    - Robust exception handling to prevent terminal crashes.
    - Optional colored terminal formatting using the 'colorama' package,
      with an elegant fallback to plain text if the package is missing.
"""

import sys
from src.cipher import encrypt, decrypt

# ==========================================
# COLORAMA INITIALIZATION & FALLBACK LOGIC
# ==========================================
# To ensure our program is "portfolio-grade", it must be exceptionally robust.
# If a user downloads this repository and runs main.py without installing 'colorama',
# we catch the ImportError and fall back to standard, plain text. This prevents crashes.
try:
    import colorama
    from colorama import Fore, Style
    colorama.init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    
    # Elegant fallback class: returns empty strings if colorama is not available
    class SafeColor:
        def __getattr__(self, name):
            return ""
            
    Fore = SafeColor()
    Style = SafeColor()

# Define visual style palettes
BANNER_COLOR = Fore.CYAN + Style.BRIGHT
MENU_COLOR = Fore.BLUE + Style.BRIGHT
PROMPT_COLOR = Fore.YELLOW + Style.BRIGHT
SUCCESS_COLOR = Fore.GREEN + Style.BRIGHT
ERROR_COLOR = Fore.RED + Style.BRIGHT
RESET = Style.RESET_ALL


def display_banner():
    """Displays a clean and professional ASCII art banner."""
    print(BANNER_COLOR + "==========================================================")
    print(BANNER_COLOR + "  🔒  CAESAR CIPHER: ENCRYPTION & DECRYPTION TOOL  🔓     ")
    print(BANNER_COLOR + "==========================================================")
    if not HAS_COLOR:
        print("[Note: Install 'colorama' for colored terminal output!]\n")


def get_menu_choice() -> int:
    """
    Displays the menu options and prompts the user for a choice.
    Performs validation to ensure the entry is valid.
    
    Returns:
        int: A validated choice (1, 2, or 3).
    """
    while True:
        print("\n" + MENU_COLOR + "--- MAIN MENU ---")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")
        
        choice_input = input(PROMPT_COLOR + "Enter your choice (1-3): ").strip()
        
        if choice_input == '1':
            return 1
        elif choice_input == '2':
            return 2
        elif choice_input == '3':
            return 3
        else:
            print(ERROR_COLOR + "❌ Invalid input. Please enter 1, 2, or 3.")


def get_shift_value() -> int:
    """
    Prompts the user for a shift value and validates it.
    Repeats the prompt if the input is not a valid integer.
    
    Returns:
        int: The validated shift key.
    """
    while True:
        try:
            shift_input = input(PROMPT_COLOR + "Enter shift value (integer key): ").strip()
            # Convert to integer. This will trigger ValueError if input is not a valid number.
            shift_value = int(shift_input)
            return shift_value
        except ValueError:
            print(ERROR_COLOR + "❌ Invalid shift key! Please enter a valid positive or negative whole number.")


def main():
    """Main execution loop of the Caesar Cipher program."""
    display_banner()
    
    # Continuous program loop
    while True:
        try:
            choice = get_menu_choice()
            
            if choice == 3:
                print("\n" + SUCCESS_COLOR + "Thank you for using the Caesar Cipher Tool! Exiting program. Goodbye! 👋")
                break
                
            # Read message from user
            message = input(PROMPT_COLOR + "Enter the message to process: ")
            
            # Read shift value
            shift = get_shift_value()
            
            print("\n" + BANNER_COLOR + "-" * 40)
            
            if choice == 1:
                # Encrypt operation
                encrypted_msg = encrypt(message, shift)
                print(SUCCESS_COLOR + "🔒 ENCRYPTION COMPLETE!")
                print(f"Original Text : {message}")
                print(f"Shift Value   : {shift}")
                print(f"Ciphertext    : " + Fore.YELLOW + Style.BRIGHT + encrypted_msg)
            elif choice == 2:
                # Decrypt operation
                decrypted_msg = decrypt(message, shift)
                print(SUCCESS_COLOR + "🔓 DECRYPTION COMPLETE!")
                print(f"Ciphertext    : {message}")
                print(f"Shift Value   : {shift}")
                print(f"Plaintext     : " + Fore.YELLOW + Style.BRIGHT + decrypted_msg)
                
            print(BANNER_COLOR + "-" * 40)
            
        except KeyboardInterrupt:
            # Handles Ctrl+C gracefully without printing a long Python traceback stack
            print("\n\n" + ERROR_COLOR + "⚠️ Program interrupted by user (Ctrl+C). Exiting safely.")
            sys.exit(0)
        except Exception as e:
            # Catch-all to make sure the loop never breaks unexpected due to runtime bugs
            print(ERROR_COLOR + f"❌ An unexpected error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
