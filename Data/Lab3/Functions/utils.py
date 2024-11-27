# File: Functions/utils.py

import shutil

def get_user_input(prompt, valid_options=None):
    """Get user input and validate it if options are provided."""
    while True:
        user_input = input(prompt)
        if valid_options and user_input not in valid_options:
            print("Invalid option. Please try again.")
        else:
            return user_input

def center_text(text, width):
    """Center the text based on the given width."""
    return '\n'.join(line.center(width) for line in text.splitlines())

def save_to_file(filename, content):
    """Save the ASCII art to a text file."""
    with open(filename, 'w') as file:
        file.write(content)
    print(f"ASCII art saved to {filename}.")

def get_terminal_width():
    """Get terminal width or fallback to a default value."""
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 80  # Default width
