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

#writing msg to file, with date info later, to be emailed
with open('msg.txt', 'w') as fout:
  for i in msg:
    fout.write(i)
    
event_date = input("What date is your event? ex. '04/06/19' ")

event_day = input("What day is your event? ex. 'Tuesday' ")

event_hr = input("What time is your event? ex. '09:15AM' ")

event_check()

correct = input("Is the above correct? ")
