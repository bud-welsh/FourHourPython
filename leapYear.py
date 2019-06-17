# Have user input a year
# Return whether or not that is a leap year

year = input("Give me a year: ")


if year % 4 == 0:
  if year % 100 == 0 and year % 400 != 0:
    print("Not a leap year.")
  else:
    print("A leap year.")
else:
  print("Not a leap year.")
