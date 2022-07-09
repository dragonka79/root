time = int(input("What time is it now, hours only, please? > "))
schedule = int(input("How many hours later should the alarm wake you up ? > "))
wake = (time + schedule) % 24
wake_afternoon = wake - 12
if wake == 0:
    print(f"The clock alarms you at midnight")
elif wake == 12:
    print(f"The clock alarms you at midday")
elif wake < 12:
    print(f"The clock alarms you at {wake} o'clock in the morning")
else:
    print(f"The clock alarms you at {wake_afternoon} o'clock in the afternoon")
