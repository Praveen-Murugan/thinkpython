"""If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at
tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?"""

import datetime
startTime = datetime.datetime(2020, 12, 19, 6, 52, 0)
# set datetime y/m/d h:m:s
timeSec = (((8.0 * 60.0) + 15.0) * 2.0) + (((7.0 * 60.0) + 12.0) * 3.0)
timeMin = timeSec / 60.0
timeSpent = datetime.timedelta(minutes=38, seconds=6)
finalTime = startTime + timeSpent

print('You get home at: ', finalTime)
