#event_planner.py: Simple event planner that emails you events you schedule

import datetime
import re
import sys
import time
import smtplib

now = datetime.datetime.now()
time_hr = now.strftime('%I:%M%p')
time_day = now.strftime('%A')
time_date = now.strftime('%D')
day_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday",
            "Saturday"]

#date check doesnt check if calender date exists
date_check1 = r"0[1-9]/0[1-9]/[1-9][0-9]"
date_check2 = r"0[1-9]/[1|2][0-9]/[1-9][0-9]"
date_check3 = r"0[1-9]/3[0-1]/[1-9][0-9]"
date_check4 = r"1[0-2]/0[1-9]/[1-9][0-9]"
date_check5 = r"1[0-2]/[1|2][0-9]/[1-9][0-9]"
date_check6 = r"1[0-2]/3[0-1]/[1-9][0-9]"

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
  print("")
  print(msg)
  print(event_date,event_day,event_hr)
  print("")

#writing msg to file, with date info later, to be emailed
with open('msg.txt', 'w') as fout:
  for i in msg:
    fout.write(i)

#creating and checking event_date validity
while True:
  try:
    event_date = input("What date is your event? ex. '04/06/19' ")
  except ValueError:
    continue
  else:
    if (re.search(date_check1,event_date) or
        re.search(date_check2,event_date) or
        re.search(date_check3,event_date) or
        re.search(date_check4,event_date) or
        re.search(date_check5,event_date) or
        re.search(date_check6,event_date)):
      break
    else:
      print("Invalid date!")
      continue

#creating and checking event_day validity
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

#creating and checking event_hr validity
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

#checking if event_check function is true
while True:
  try:
    correct = input("Is the above correct? ")
  except ValueError:
    continue
  else:
    if correct == "Yes":
      print("")
    elif correct == "No":
      print("")
    else:
      print("Sorry, please choose 'Yes' or 'No'.")

time.sleep(1.5)
sys.exit(0)
