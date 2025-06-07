def perform_operation(operation, num1, num2):
    """
    Perform arithmetic operations based on the provided operation type.
    
    Parameters:
    operation (str): The type of operation to perform ('add', 'subtract', 'multiply', 'divide').
    num1 (int or float): The first number.
    num2 (int or float): The second number.

    Returns:
    int or float: The result of the arithmetic operation.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero error"
    else:
        return "Invalid operation"