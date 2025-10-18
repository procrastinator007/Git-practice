"""
main.py
Author: Jai Patel
Description: A simple Python script to demonstrate GitHub version control,
branching, and collaboration features.
"""

import datetime

def greet_user(name: str) -> None:
    """Prints a friendly greeting message with timestamp."""
    now = datetime.datetime.now()
    print(f"Hello, {name}! 👋")
    print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print("This is a test commit from main.py — demonstrating GitHub workflow.")

def main():
    print("=== Welcome to Jai Patel's GitHub Demo Project ===")
    user_name = input("Enter your name: ").strip()
    greet_user(user_name)
    print("\nTry making a new branch and modifying this message!")

if __name__ == "__main__":
    main()
