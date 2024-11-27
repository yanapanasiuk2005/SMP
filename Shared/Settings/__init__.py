# File: InitFile/__init__.py

import os

def initialize_app():
    """Perform any initialization tasks like setting up configurations or environment variables."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the ASCII Art Generator!")
