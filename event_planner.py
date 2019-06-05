#event_planner.py: Simple event planner that emails you events you schedule

import datetime
import re

now = datetime.datetime.now()
day_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday",
            "Saturday"]

#date check doesnt check if calender date exists
date_check = r"[1-12]/[1-31]/[19-99]"

#checking 12 hr clock
hr_check1 = r"0[0-9]:[0-5][0-9][AM|PM]"
hr_check2 = r"1[0-2]:[0-5][0-9][AM|PM]"

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

while True:
  try:
    event_date = input("What date is your event? ex. '04/06/19' ")
  except ValueError:
    continue
  else:
    if re.search(date_check,event_date):
      break
    else:
      print("Invalid date!")
      continue

while True:
  try:
    event_day = input("What day is your event? ex. 'Tuesday' ")
  except ValueError:
    continue
  else:
    if event_day in day_list:
      break
    else:
      print("Sorry, that day doesn't exist.")
      continue

while True:
  try:
    event_hr = input("What time is your event? ex. '09:15AM' ")
  except ValueError:
    continue
  else:
    if re.search(hr_check1,event_hr) or re.search(hr_check2,event_hr):
      break
    else:
      print("Sorry, that time doesn't exist.")
      continue
            
event_check()

correct = input("Is the above correct? ")
