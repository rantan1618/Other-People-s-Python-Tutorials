import datetime

print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime',
# 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

mill = datetime.date(2000, 1, 1)
# Let's assume that it took 100 days for people to feel normal after Y2K.
# Create a time delta object and pass in the number of days.
# a positive number will increase the date and a negeitive number will decrease the date.
dt = datetime.timedelta(100)
# Sum the two variables.
print(mill + dt)

print(gvr.strftime("%A, %B %d, %Y"))

message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr))


launch_date = datetime.date(2017, 3, 30)
launch_time = datetime.time(22, 27, 0)
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)

print(launch_date)
print(launch_time)
print(launch_datetime)

now =  datetime.datetime.today()
print(now)
# Access time down to the Microsecond with:
print(now.microsecond)

# Convert Strings to datetime Objects
moon_landing = "7/20/1969"
moon_landing_datetime = datetime.datetime.strptime(moon_landing, "%m/%d/%Y")
print(moon_landing_datetime)

# The datetime module contains a Class called Time Delta which can store the difference between two datetimes.
# It can also be used to add or subtract the datetime of other objects.