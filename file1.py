import operator

# Dictionary mapping operator symbols to their corresponding functions
OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(num1, num2, op_symbol):
    """
    Performs the specified arithmetic operation on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        op_symbol (str): The operator symbol ('+', '-', '*', '/').

    Returns:
        float or None: The result of the operation, or None if an error occurs.
    """
    # 1. Check for a valid operator
    operation_func = OPERATORS.get(op_symbol)
    if operation_func is None:
        return None, f"Error: Invalid operator '{op_symbol}'. Please use +, -, *, or /."

    # 2. Handle division by zero
    if op_symbol == '/' and num2 == 0:
        return None, "Error: Cannot divide by zero."

    # 3. Perform the calculation
    try:
        result = operation_func(num1, num2)
        return result, None # Return the result and no error message
    except Exception as e:
        return None, f"An unexpected calculation error occurred: {e}"


def main():
    """
    Main loop for the calculator application, prompting for two numbers 
    and an operation repeatedly.
    """
    print("--- Two-Number Arithmetic Calculator ---")
    print("Available operations: +, -, *, /")
    print("Type 'exit' or 'quit' at any prompt to stop.")
    print("-" * 40)

    while True:
        try:
            # 1. Get the first number
            num1_input = input("Enter the first number: ").strip()
            if num1_input.lower() in ['exit', 'quit']:
                break
            num1 = float(num1_input)

            # 2. Get the operator
            op_symbol = input("Enter the operator (+, -, *, /): ").strip()
            if op_symbol.lower() in ['exit', 'quit']:
                break

            # 3. Get the second number
            num2_input = input("Enter the second number: ").strip()
            if num2_input.lower() in ['exit', 'quit']:
                break
            num2 = float(num2_input)

            # 4. Calculate the result
            result, error_message = calculate(num1, num2, op_symbol)

            # 5. Display output
            if error_message:
                print(error_message)
            else:
                # Format the output to two decimal places for cleanliness
                print(f"\nResult: {num1} {op_symbol} {num2} = {result:.2f}")

        except ValueError:
            print("Invalid input. Please ensure you enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred during input: {e}")

    print("\nCalculator closed. Goodbye!")

# Ensure the main function runs only when the script is executed directly


main()


