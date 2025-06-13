def safe_divide(float(numerator), float(denominator)):
    try:
        if denominator <= 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        else:
            return numerator / denominator
    except ValueError:
        return "Please enter numeric values only"
