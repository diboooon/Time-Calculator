def add_time(start, duration, starting_day=None):
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))
    
    # Calculate total minutes
    total_minutes = start_hour * 60 + start_minute
    
    # Add duration time
    total_minutes += duration_hour * 60 + duration_minute
    
    # Calculate days and remaining minutes
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)
    
    # Calculate new time
    new_hour = remaining_minutes // 60
    new_minute = remaining_minutes % 60
    
    # Determine the new period (AM or PM)
    new_period = "AM" if (start_hour < 12 and new_hour < 12) or (start_hour == 12 and new_hour == 0) else "PM"
    
    # Adjust new_hour to 12-hour format
    new_hour = new_hour % 12
    new_hour = new_hour if new_hour != 0 else 12
    
    # Determine the new day of the week if starting_day is provided
    if starting_day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        starting_day_index = days_of_week.index(starting_day.lower().capitalize())
        new_day_index = (starting_day_index + days) % 7
        new_day = days_of_week[new_day_index]
        if days == 1:
            new_day = new_day.lower()
    
    # Generate the result string
    result = f"{new_hour:02d}:{new_minute:02d} {new_period}"
    if starting_day:
        result += f", {new_day}"
    if days == 1:
        result += " (next day)"
    elif days > 1:
        result += f" ({days} days later)"
    
    return result
