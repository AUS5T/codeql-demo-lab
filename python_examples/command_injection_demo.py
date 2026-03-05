# Intentionally insecure example for CodeQL demo purposes only.
# Demonstrates command injection risk.

import os

def list_directory(user_input):
    # Vulnerable: user input passed directly to shell command
    os.system("ls " + user_input)

if __name__ == "__main__":
    user_input = input("Enter directory name: ")
    list_directory(user_input)
