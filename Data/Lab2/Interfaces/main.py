from Data.Lab1.Functions.memory_functions import memory_save, memory_clear, memory_recall
from Data.Lab2.Classes.Calculator import Calculator
from Data.Lab2.Functions.history_functions import log_history, clear_history, view_history
from Data.Lab2.Functions.memory_functions import settings
from Shared.Settings.user_settings import format_result, set_decimal_places, toggle_auto_memory_clear, \
    toggle_auto_memory_save


def display_menu():
    print("\n🧮  Welcome to the Friendly Calculator!")
    print("Please select an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exponentiation (x^y)")
    print("6. Square Root (√x)")
    print("7. Remainder (x % y)")
    print("M+. Save to Memory")
    print("MR. Recall from Memory")
    print("MC. Clear Memory")
    print("H. View History")
    print("CH. Clear History")
    print("S1. Set Decimal Places")
    print("S2. Toggle Auto Memory Save")
    print("S3. Toggle Auto Memory Clear")
    print("Q. Quit")


def handle_choice(choice, calc):
    if choice in ['1', '2', '3', '4', '5', '7']:
        num1 = float(input("🔢 Enter the first number: "))
        #operator = input("✍️  Enter operator (+, -, *, /, ^, %): ")
        num2 = float(input("🔢 Enter the second number: "))

        if choice == '1':
            result = calc.add(num1, num2)
            print(f"🔍 Result: {num1} + {num2} = {format_result(result)}")
            log_history(f"{num1} + {num2}", format_result(result))
        elif choice == '2':
            result = calc.subtract(num1, num2)
            print(f"🔍 Result: {num1} - {num2} = {format_result(result)}")
            log_history(f"{num1} - {num2}", format_result(result))
        elif choice == '3':
            result = calc.multiply(num1, num2)
            print(f"🔍 Result: {num1} * {num2} = {format_result(result)}")
            log_history(f"{num1} * {num2}", format_result(result))
        elif choice == '4':
            result = calc.divide(num1, num2)
            print(f"🔍 Result: {num1} / {num2} = {format_result(result)}")
            log_history(f"{num1} / {num2}", format_result(result))
        elif choice == '5':
            result = calc.exponentiate(num1, num2)
            print(f"🔍 Result: {num1} ^ {num2} = {format_result(result)}")
            log_history(f"{num1} ^ {num2}", format_result(result))
        elif choice == '7':
            result = calc.remainder(num1, num2)
            print(f"🔍 Result: {num1} % {num2} = {format_result(result)}")
            log_history(f"{num1} % {num2}", format_result(result))

        if settings["auto_memory_save"]:
            memory_save(format_result(result))

    elif choice == '6':
        num = float(input("🔢 Enter number for square root (√): "))
        result = calc.sqrt(num)
        print(f"🔍 Result: √{num} = {format_result(result)}")
        log_history(f"√{num}", format_result(result))

        if settings["auto_memory_save"]:
            memory_save(format_result(result))

    elif choice == 'M+':
        memory_save(calc.get_last_result())
    elif choice == 'MR':
        memory_recall()
    elif choice == 'MC':
        memory_clear()
    elif choice == 'H':
        view_history()
    elif choice == 'CH':
        clear_history()
    elif choice == 'S1':
        set_decimal_places()
    elif choice == 'S2':
        toggle_auto_memory_save()
    elif choice == 'S3':
        toggle_auto_memory_clear()
    elif choice == 'Q':
        print("👋 Exiting the calculator. Goodbye!")
        return False
    else:
        print("❌ Invalid input. Please enter a valid choice.")
    return True


def run_calculator():
    calc = Calculator()
    continue_calculation = True

    while continue_calculation:
        display_menu()
        choice = input("🔽 Enter your choice: ")
        continue_calculation = handle_choice(choice, calc)
