"""
Assessment1-Programming-Skills-Portfolio Exercise 5: Days of the Month
"""


# Dictionary storing the number of days for each month
months = {
    "1": 31,  # January
    "2": 28,  # February (default, not considering leap years yet)
    "3": 31,  # March
    "4": 30,  # April
    "5": 31,  # May
    "6": 30,  # June
    "7": 31,  # July
    "8": 31,  # August
    "9": 30,  # September
    "10": 31, # October
    "11": 30, # November
    "12": 31  # December
}

# Loop until a valid month number is entered
while True:
    try:
        # Prompt user to enter a month number
        month = int(input("Enter month number (1-12): "))
        
        # Check if the entered month number is valid
        if 1 <= month <= 12:
            break  # Exit loop if valid
        else:
            print("Invalid month. Please enter a number between 1 and 12.")
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid number.")

# Prompt user to indicate if the year is a leap year
choice = input("Is the year a leap year? [Y/N]: ")
if choice.lower() == "y":
    # If it's a leap year, update February to have 29 days
    months["2"] = 29

# Output the number of days in the selected month
print(f"The number of days in month {month} is {months[str(month)]}.")
