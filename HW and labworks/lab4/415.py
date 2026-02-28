import datetime

def is_leap_year(year: int):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

birth_day, time_zone1_str = input().split()
current_day, time_zone2_str = input().split()

birth_day = datetime.datetime.strptime(birth_day, "%Y-%m-%d")
current_day = datetime.datetime.strptime(current_day, "%Y-%m-%d")

time_zone1 = datetime.timedelta(
        hours=int(time_zone1_str[4:6]),
        minutes=int(time_zone1_str[7:9])
        )

if time_zone1_str[3] == '-':
    time_zone1 = -time_zone1

time_zone2 = datetime.timedelta(
        hours=int(time_zone2_str[4:6]),
        minutes=int(time_zone2_str[7:9])
        )

if time_zone2_str[3] == '-':
    time_zone2 = -time_zone2


birth_day -= time_zone1
current_day -= time_zone2

if birth_day.month < current_day.month or birth_day.month == current_day.month and birth_day.day < current_day.day:
    birth_day = birth_day.replace(year=current_day.year+1)
else:
    birth_day = birth_day.replace(year=current_day.year)

delta_days = (birth_day - current_day).days
if birth_day.hour - current_day.hour > 0 or birth_day.minute - current_day.minute > 0:
    delta_days += 1

print(delta_days)