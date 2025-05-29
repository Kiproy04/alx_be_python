task = input("Enter a task description ")
priority = input("How do you priortize this task? (high, medium, low) ")
time_bound = input("Is the task time bound (yes or no) ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task consider completing it when you have free time.")