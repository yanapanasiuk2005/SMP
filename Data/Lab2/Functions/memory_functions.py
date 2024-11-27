settings = {
    "decimal_places": 2,
    "auto_memory_save": False,
    "auto_memory_clear": False
}

def set_decimal_places():
    try:
        decimal_places = int(input("Enter number of decimal places: "))
        if 0 <= decimal_places <= 10:
            settings["decimal_places"] = decimal_places
            print(f"Decimal places set to {decimal_places}.")
        else:
            print("Enter a number between 0 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")
