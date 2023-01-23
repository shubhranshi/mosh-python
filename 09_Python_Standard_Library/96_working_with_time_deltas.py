# Time delta represents duration
from datetime import datetime,timedelta
import time

dt1 = datetime(2020,5,15,18,40,50)  # year, month, day, hour, minute, second
print(dt1)

dt2 = datetime.now()
print(dt2)

duration = dt2 - dt1
print(duration) # 849 days, 16:36:11.336788
print("Days:", duration.days)   # .days --> days is an attribute, gives 849
print("Seconds:", duration.seconds)    # seconds is an attribute, gives 60761 (representing "16:36:11")
print("Total Seconds:", duration.total_seconds())   # total_seconds() is a method, gives total duration in seconds.
# we do not have month and year here in timedeltas, because, we can have varying amount of time in year or month.


# We can also add a "timedelta" object to a "datetime" object
dt3 = datetime(2022,9,12) + timedelta(1)    # adds one day, gives 2022-09-13 00:00:00
print(dt3)

# can also give keyword arguments to make it more clear
dt4 = datetime(2022,9,12) - timedelta(days=15)    # subtracts 15 day, gives 2022-08-28 00:00:00
print(dt4)

dt5 = datetime(2022,9,12) + timedelta(days=1, seconds=100)    # gives 2022-09-13 00:01:40
print(dt5)