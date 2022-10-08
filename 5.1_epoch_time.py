'''

5.1) Write a script that reads the current time and converts it to
a time of day in hours, minutes, and seconds, plus the number of days since
the epoch.
'''

import time

epoch = time.time()
seconds_day = 24 * 60 * 60
seconds_hour = 60 * 60
seconds_minute = 60

days = epoch // seconds_day
hours = (epoch % seconds_day) // seconds_hour -4
minutes = (epoch % seconds_day) % seconds_hour // seconds_minute
seconds = (epoch % seconds_day) % seconds_hour % seconds_minute
print("%s: %s: %s: %s" %(days, hours, minutes, seconds))
print("Boston Current time is %d: %d: %d: %d" %(days, hours, minutes, seconds))
