#event_planner.py: Simple event planner that emails you events you schedule

import datetime

now = datetime.datetime.now()
msg = ""

#reading event.txt file
with open('event.txt', 'r') as fin:
  event = fin.readlines()
  for i in event:
    msg += i

#function to check event, event day, event date, and event time
def event_check():    
  print(msg)
  print("")
  print(time_date,time_day,time_hr)
