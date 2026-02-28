import datetime

start, time1, time_zone1_str = input().split()
end, time2, time_zone2_str = input().split()

start += time1
end += time2

datetime_format = "%Y-%m-%d%H:%M:%S"
start = datetime.datetime.strptime(start, datetime_format)
end = datetime.datetime.strptime(end, datetime_format)

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

start -= time_zone1
end -= time_zone2

seconds = (end - start).total_seconds()

print(int(seconds))