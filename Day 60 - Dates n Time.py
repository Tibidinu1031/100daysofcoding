import datetime

while True:
  print()
  print("EVENT DELTA CALCULATOR")
  today = datetime.date.today()
  print(f"Today is: {today}")
  print()
  
  event_name = input("Enter event name: ")
  day = int(input("Enter day: "))
  month = int(input("Enter month: "))
  year = int(input("Enter Year: "))
  fullTime = datetime.date(year, month, day)

  difference = (fullTime - today).days

  if fullTime > today:
    print(f"You have {difference} days left until {event_name}")
  elif fullTime < today:
    print(f"{event_name} in the past and you missed it by {abs(difference)} days")
  else:
    print(f"{event_name} is today!!! 🥳🥳🥳🥳🥳🥳🥳")