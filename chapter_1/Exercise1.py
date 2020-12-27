"""If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time per mile? What
is your average speed in miles per hour? (Hint: there are 1.61 kilometers in a mile)"""

distance_in_Km = 10.0
distance_in_Miles = (distance_in_Km * (1.0 / 1.61))
seconds = ((43.0 * 60.0) + 30.0)
hours = (43.5 / 60.0)

def timePerMile(distance_in_Miles, seconds):
   print(seconds / distance_in_Miles, 'seconds per mile')

def avgSpeed(distance_in_Miles, hours):
   print (distance_in_Miles / hours, 'miles per hour')

timePerMile(distance_in_Miles, seconds)
avgSpeed(distance_in_Miles, hours)



