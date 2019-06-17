# Have user input a year
# Return whether or not that is a leap year

year = input("Give me a year: ")

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
      leap = False
    else:
      leap = True

    return leap

