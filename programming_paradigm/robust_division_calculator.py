def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator <= 0:
            return ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            result = numerator / denominator
            return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
