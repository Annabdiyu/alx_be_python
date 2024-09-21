task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ")
time_bound=input("Is it time-bound? (yes/no): ")
match priority:
    case "high":
        if time_bound=="yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound:
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
     