print("How many seconds are in a year (calculated month by month):")
print("-------------------------------")
seconds_in_a_minute = 60
minutes_in_an_hour = 60
hoursPerDay = 24
daysPerFebruary = 28
daysPerShortMonths = 30
daysPerLongMonths = 31
print("")

print("--------------")
print("")
seconds_in_february = (seconds_in_a_minute * minutes_in_an_hour * hoursPerDay * daysPerFebruary)
print("Seconds in February: ", seconds_in_february)
print("")
seconds_in_short_months = (seconds_in_a_minute * minutes_in_an_hour * hoursPerDay * daysPerShortMonths * 4)
print("Seconds In Short Months: ", seconds_in_short_months)
print("")
seconds_in_long_months = (seconds_in_a_minute * minutes_in_an_hour * hoursPerDay * daysPerShortMonths * 7)
print("Seconds in Long Months: ", seconds_in_long_months)
print("")
print("Seconds in a year: ",seconds_in_february + seconds_in_short_months + seconds_in_long_months)
print("")
print("-------------------------------")
print("How many seconds are in a year (calculated with 365 days):")
print("")
leapYear = input("Is it a leap year? ")
if leapYear == "yes" or leapYear == "Yes":
  print(seconds_in_a_minute * minutes_in_an_hour * hoursPerDay * 366)
else: 
  print("Total seconds in a year: ",seconds_in_a_minute * minutes_in_an_hour * hoursPerDay * 365)