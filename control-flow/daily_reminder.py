Task = input("Enter a task description ")
Priority = input("How do you priortize this task? (high, medium, low) ")
Time_bound = input("Is the task time bound (yes or no) ")

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