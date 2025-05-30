Task = str(input("Enter your task: "))
Time_Bound = str(input("Is it time-bound? (yes or no) "))
Priority = str(input("(high, medium, low) "))

match Priority:
    case "high":
        if Time_Bound == "yes":
            print(f"{Task} is a {Priority} priority task that requires immediate attention today! ")
        else:
            print(f"{Task} is a {Priority} priority task consider completing it when you have free time.")
    case "medium":
        if Time_Bound == "yes":
            print(f"{Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"{Task} is a {Priority} priority task consider completing it when you have free time.")
    case "low":
        if Time_Bound == "yes":
            print(f"{Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"{Task} is a {Priority} priority task consider completing it when you have free time.")
    case _:
        print("Invaid input")