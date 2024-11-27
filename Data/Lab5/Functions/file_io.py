# Functions/file_io.py

def save_to_file(filename, ascii_art):
    try:
        with open(filename, 'w') as file:
            file.write(ascii_art)
        print(f"ASCII art saved to {filename}")
    except IOError as e:
        print(f"Error saving to file: {e}")
