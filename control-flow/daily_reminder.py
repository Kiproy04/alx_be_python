Task = input("Enter your task: ")
Time_bound = input("Is it time-bound? (yes or no) ")
Priority = input("How do you priortize this task? (high, medium, low) ")

match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"{Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"{Task} is a {Priority} priority task consider completing it when you have free time.")
    case "medium":
        if Time_bound == "yes":
            print(f"{Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"{Task} is a {Priority} priority task consider completing it when you have free time.")
    case "low":
        if Time_bound == "yes":
            print(f"{Task} is a {Priority} priority task that requires immediate attention today!")
        else:
            print(f"{Task} is a {Priority} priority task consider completing it when you have free time.")
    case _:
        print("Invaid input")