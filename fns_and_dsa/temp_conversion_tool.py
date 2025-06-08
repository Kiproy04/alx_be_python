CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius + 32) * CELSIUS_TO_FAHRENHEIT_FACTOR

if __name__ == "__main__":
    print("Welcome to the Temperature Conversion Tool!")

    try:
        temperature = float(input("Enter the temperature to convert: "))
        c_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
        if c_f == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif c_f == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            print("Invalid input. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")