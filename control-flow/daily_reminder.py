task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ").lower()
time_bound=input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        if time_bound=="yes":
            print("Reminder: your task is a high priority task that requires immediate attention today!")
        else:
            print("Reminder: your task is high priority task ,so consider finishinig it on time.")
    case "medium":
        if time_bound=="yes":
            print("Reminder: your task i a medium priority task that requires immediate attention today!")
        else:
            print("Reminder: your task is medium priority task ,so consider finishinig it on time.")
    case "low":
        if time_bound:
            print("Note: your task is a low priority task. Consider completing it when you have free time.")
        else:
            print("Reminder: your task is low priority task ,so consider finishinig it on time.")
     