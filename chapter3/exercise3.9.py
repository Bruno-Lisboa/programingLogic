# turn days in hours, minutes and seconds
days = int(input("Put the days here: "))
hours = int(input("Put the hours here: "))
minutes = int(input("Put the minutes here: "))
seconds = int(input("Put the seconds here: "))

daysToSeconds = days * 24 * 60 * 60
hoursToSeconds = hours * 60 * 60
minutesToSeconds = minutes * 60

print(f"{days} days {hours} hours {minutes} minutes and {seconds} seconds are {daysToSeconds + hoursToSeconds + minutesToSeconds + seconds} seconds")
