import calendar

days = list(calendar.day_name)
x = 2

def day_name(x):
    """Get the index of the day of the week and returns with its name"""
    if x >= 0 and x <= 6:
        return days[x]
    else:
        print("The name of the day of this index does not exist, give me a \
number between [0, 6].")
        exit()

start_day = int(input("What day have you left on, index of the day, pls.?> "))
day_name(start_day)
end_day = int(input("How many days were you away for?> "))
day_return = (start_day + end_day) % 7


print(day_name(day_return))





