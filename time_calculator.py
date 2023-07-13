def add_time(start, duration, day=""):

    # apply uniformity to the day
    day = day.capitalize()
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    #split into time and meridian
    start_time, meridian = start.split()
  
    #split into hour and minute components
    hour1, minute1 = map(int, start_time.split(":"))
    hour2, minute2 = map(int, duration.split(":"))

    #calculate new values
    new_hour = hour1 + hour2
    new_minute = minute1 + minute2

    # add hour if minute value is 60 or higher
    if new_minute >= 60:
        new_minute -= 60
        new_hour += 1

    # days later is the hour value / 24, // is used because it returns an int without a decimal 
    days_later = new_hour // 24
    # update hour to modulous of 24
    new_hour %= 24

    # account for passing into the next day
    if meridian == "PM" and new_hour >= 12:
        days_later += 1
    
    # hour is the remainder of hour/12, account for midnight being 0
    new_hour %= 12
    if new_hour == 0:
        new_hour = 12

    # switch from AM to PM
    new_meridian = "AM"
    if start.endswith("PM") and (hour1 + hour2) >= 12:
        new_meridian = "PM"

    # initialize full_days_later string  
    full_days_later = ""

    # if there is a day (optional third argument) 
    if day != "":
        # index the day, find days later % 7
        index = days.index(day)
        new_day_index = (index + days_later) % 7
        new_day = days[new_day_index]
        full_days_later = f", {new_day}"

    # concatenate string
    new_time = f"{new_hour}:{str(new_minute).rjust(2, '0')} {new_meridian}{full_days_later}"

    # if days_later is 1, display next day
    # if it's more than 1, show by how many days
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    #return the string
    return new_time
