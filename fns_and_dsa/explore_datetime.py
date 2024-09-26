# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format as 'YYYY-MM-DD HH:MM:SS'
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Prompt user for input
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate future date
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        # Format and print the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

# Run the functions
if __name__ == "__main__":
    display_current_datetime()  # Display current date and time
    calculate_future_date()  # Calculate and display future date
