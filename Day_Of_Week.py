# This Program will ask a user to input the day of week
# If it is a weekday it will print "It's a weekday"
 # If it is a weekend it will print "It's the weekend"

import datetime
today = datetime.datetime.now()
day = today.weekday()


dayname = {0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}

print("Today is ", dayname[day])

if day <= 4:
     print("It is a Weekday")
else:
     print("It is the Weekend!!!")


