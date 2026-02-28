from datetime import datetime, timedelta

def parse(line):
    date_part, tz_part = line.split()
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    sign = 1 if '+' in tz_part else -1
    hours, minutes = map(int, tz_part[4:].split(':'))
    offset = timedelta(hours=hours, minutes=minutes)
    if sign == 1:
        dt = dt - offset
    else:
        dt = dt + offset
    return dt
line1 = input().strip()
line2 = input().strip()
dt1 = parse(line1)
dt2 = parse(line2)
difference = abs(dt1 - dt2)
print(difference.days)