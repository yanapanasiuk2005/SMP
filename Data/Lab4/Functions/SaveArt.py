def save_ascii_art_to_file(art):
    save_option = input("Would you like to save the ASCII art to a text file? (yes/no): ").lower()
    if save_option == "yes":
        file_name = input("Enter the filename (without extension): ") + ".txt"
        try:
            with open(file_name, 'w') as file:
                file.write(art)
            print(f"ASCII art successfully saved to {file_name}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
