"""
Python sets - actions
"""

weekdays = {'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'}
sport_days = {'Sun', 'Wed'}
lecture_days = {'Mon', 'Wed', 'Fri'}

sport_and_lecture_days = sport_days.intersection(lecture_days)
print(f"\nDays with sport and lectures: "
      f"{sport_and_lecture_days}\n")


busy_days = sport_days.union(lecture_days)
print(f"\nBusy days: {busy_days}\n")


free_days = weekdays.difference(busy_days)
print(f"\nFree days: {free_days}\n")

