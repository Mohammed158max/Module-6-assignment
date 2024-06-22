import sys
from datetime import datetime, timedelta

# Part 1: Process input data and print item and cost
def process_input():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            date, time, store, item, cost, payment = data
            print(f"{item}\t{cost}")

# Part 2: Add timedelta to datetime and subtract 60 seconds, then add 2 years
def timedelta_operations():
    now = datetime.now()
    print("Current datetime:", now)
    
    # Add 1 day
    one_day_later = now + timedelta(days=1)
    print("One day later:", one_day_later)
    
    # Subtract 60 seconds
    minus_sixty_seconds = now - timedelta(seconds=60)
    print("60 seconds earlier:", minus_sixty_seconds)
    
    # Add 2 years (730 days as an approximation for 2 years)
    two_years_later = now + timedelta(days=730)
    print("Two years later:", two_years_later)

# Part 3: Create a timedelta object representing 100 days, 10 hours, and 13 minutes
def create_timedelta():
    delta = timedelta(days=100, hours=10, minutes=13)
    print("Timedelta:", delta)

# Part 4: Function to add feet and inches to a datetime object
def add_feet_inches_to_datetime(feet, inches, base_datetime=None):
    if base_datetime is None:
        base_datetime = datetime.now()
    
    total_inches = (feet * 12) + inches
    seconds_to_add = total_inches * 60  # Assuming each inch represents 60 seconds for this example
    result_datetime = base_datetime + timedelta(seconds=seconds_to_add)
    return result_datetime

def main():
    # Part 1
    # Uncomment the following line if you are running the script with input from sys.stdin
    # process_input()
    
    # Part 2
    timedelta_operations()
    
    # Part 3
    create_timedelta()
    
    # Part 4
    feet = 5
    inches = 8
    datetime_object = datetime.now()
    print("Current datetime:", datetime_object)
    print("Updated datetime:", add_feet_inches_to_datetime(feet, inches))

if __name__ == "__main__":
    main()
