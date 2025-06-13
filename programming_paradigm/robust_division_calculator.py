def safe_divide(float(numerator), float(denominator)):
    try:
        if denominator <= 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        else:
            return numerator / denominator
    except ValueError:
        print("Error: Please enter numeric values only")
