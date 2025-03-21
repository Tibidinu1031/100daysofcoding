print("Virtual Encourager")
print("-----------------")
name = input("What is your name? ")
if name == "John" or name == "john":
  day = input("Hello " + name + " What day is it today? > ")
  if day == "Monday" or day == "monday":
    print("Happy Monday, go kill it! That's the best of day of the week, jokes aside")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Monday coding " + name + "! You're going to have a great day!")
  elif day == "Tuesday" or day == "tuesday":
    print("Monday's over, Tuesday's here, go kill it as you did yesterday!")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Tuesday coding " + name + "! You're going to have a great day!")
  elif day == "Wednesday" or day == "wednesday":
    print(name + " You're killing it ma' man. Keep up the good work, " + name + ", ok?")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Wednesday coding " + name + "! You're going to have a great day!")
  elif day == "Thursday" or day == "thursday":
    print("Halfway there, you got it under control mate")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Thursday coding " + name + "! You're going to have a great day!")
  elif day == "Friday" or day == "friday":
    print("Last day of hunting season, finish it up the way you've been rocking it")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Friday coding " + name + "! You're going to have a great day!")
  elif day == "Saturday" or day == "saturday":
    activity = input("What are you going to do today? > ")
    print("Farming time " + name + "-boy! On with the learning now!")
    if activity == "Learn" or activity == "learn":
      print("Saturday learning " + name + "! You're going to have a great day!")
  else:
    print("Reflection day my good man! Time to prepare the week ahead. Gotta feeling it gonn' be as good as the last one! Take care!")
    activity = input("What are you going to do today? > ")
  if activity == "Reflect" or activity == "reflect":
    print("Sunday reflecting " + name + "! You're going to have a great day!")
elif name == "Jane" or name == "jane":
  day = input("Hello " + name + " What day is it today? > ")
  if day == "Monday" or day == "monday":
    print("Happy Monday " + name + "! That's the best of day of the week, jokes aside")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Monday coding " + name + "! You're going to have a great day!")
  elif day == "Tuesday" or day == "tuesday":
    print("Monday's over " + name + ". Tuesday's here, go kill it as you did yesterday!")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Tuesday coding " + name + "! You're going to have a great day!")
  elif day == "Wednesday" or day == "wednesday":
    print(name + " You're killing it ma'am. Keep up the good work, " + name + ", ok?")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Wednesday coding " + name + "! You're going to have a great day!")
  elif day == "Thursday" or day == "thursday":
    print("Halfway there, you got it under control ma'am!")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Thursday coding " + name + "! You're going to have a great day!")
  elif day == "Friday" or day == "friday":
    print("Last day of hunting season, " + name + ", finish it up the way you've been rocking it")
    activity = input("What are you going to do today? > ")
    if activity == "Code" or activity == "code":
      print("Friday coding " + name + "! You're going to have a great day!")
  elif day == "Saturday" or day == "saturday":
    print("Farming time, " + name + "! On with the learning now!")
    activity = input("What are you going to do today? > ")
    if activity == "Learn" or activity == "learn":
      print("Saturday learning " + name + "! You're going to have a great day!")
  else:
    print("Reflection day me lady! Time to prepare the week ahead. Gotta feeling it gonn' be as good as the last one! Take care!")
    activity = input("What are you going to do today? > ")
    if activity == "Reflect" or activity == "reflect":
      print("Sunday reflecting " + name + "! You're going to have a great day!")
else:
  print("think again ", name)