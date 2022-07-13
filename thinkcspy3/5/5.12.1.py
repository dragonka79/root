import calendar

days = list(calendar.day_name)
x = 2

def day_name(x):
    """Get the index of the day of the week and returns with its name"""
    if x >= 0 and x <= 6:
        print(days[x])
    else:
        print("The name of the day of this index does not exist, give me a \
number between [0, 6].")

day_name(x)

