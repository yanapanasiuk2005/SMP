# Interfaces/menu.py
from Data.Lab5.Classes.Test import Cube
from Data.Lab5.Functions.file_io import save_to_file


def display_menu():
    print("\n--- Shape Rotation, Size, Color, and Save Menu ---")
    print("1. Select Shape (Cube)")
    print("2. Select Rotation Axis (X, Y, Z)")
    print("3. Set Rotation Angle (in degrees)")
    print("4. Choose Shape Color (Red, Green, Blue, etc.)")
    print("5. Set Shape Size (Scale Factor)")
    print("6. Display Shape")
    print("7. Save Shape ASCII Art to a File")
    print("8. Exit")


def menu5():
    shape = Cube()  # Default shape
    axis, angle, color, scale = 'y', 0, 'white', 1.0

    while True:
        display_menu()
        choice = input("Select an option (1-8): ")

        if choice == '1':
            print("Cube selected.")
        elif choice == '2':
            axis = input("Enter rotation axis (x, y, or z): ").lower()
        elif choice == '3':
            angle = float(input(f"Enter rotation angle in degrees for {axis}-axis: "))
            shape.set_rotation_angle(angle, axis)
        elif choice == '4':
            color = input("Choose a color (red, green, etc.): ").lower()
            shape.set_color(color)
        elif choice == '5':
            scale = float(input("Enter scale factor (e.g., 0.5 for smaller, 2 for larger): "))
            shape.set_scale(scale)
        elif choice == '6':
            shape.rotate()
            shape.draw()
        elif choice == '7':
            filename = input("Enter filename to save ASCII art (e.g., shape.txt): ")
            ascii_art = shape.draw(to_file=True)
            save_to_file(filename, ascii_art)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please select a valid option.")
