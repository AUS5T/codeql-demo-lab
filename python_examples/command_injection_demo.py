import os

def list_directory(user_input):
    # Intentionally insecure example for CodeQL demonstration
    command = "ls " + user_input
    os.system(command)

if __name__ == "__main__":
    user_value = input("Enter directory name: ")
    list_directory(user_value)
