"""
Write a correct version of increment that doesn’t contain any loop
"""
class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30


def increment(time, seconds):
    time.second += seconds

    add_mins, remain_seconds = divmod(time.second, 60)
    time.minute += add_mins
    time.second = remain_seconds

    add_hours, remain_minute = divmod(time.minute, 60)
    time.hour += add_hours
    time.minute = remain_minute
