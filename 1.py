
# This program converts seconds to hours, minutes and seconds

seconds = int(input('Give me the seconds > '))

hours = seconds // 3600
seconds_leftover_hours = seconds % 3600
minutes = seconds_leftover_hours // 60
seconds_leftover_minutes = seconds_leftover_hours % 60

print(f"""The {seconds} seconds equals to {hours} hours, {minutes} minutes 
and {seconds_leftover_minutes} seconds""")
