num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":
        answer = num1 + num2
        print(f"The result is {answer}")
    case "-":
        answer = num1 - num2
        print(f"The result is {answer}")
    case "*":
        answer = num1 * num2
        print(f"The result is {answer}")    
    case "/":
        if num2 == 0:
            print("Cannot be divided by 0")
        answer = num1 / num2
        print(f"The result is {answer}")
    case _:
        print("Invalid operation! Try again")