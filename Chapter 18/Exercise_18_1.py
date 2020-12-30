"""
Write a __cmp__ method for Time objects. Hint: you can use tuple comparison, but
you also might consider using integer subtraction

"""
class Time(object):
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    def __lt__(self, other):
      return (self.hour, self.minute) < (other.hour, other.minute)

    def __gt__(self, other):
      return (self.hour, self.minute) > (other.hour, other.minute)

    def __eq__(self, other):
      return (self.hour, self.minute) == (other.hour, other.minute)

    def __repr__(self):
      return '{}'.format((self.hour, self.minute))

a = Time(hour=3, minute=31)
b = Time(hour=4, minute=30)

print(a < b)
