print("Hello World")

name = raw_input("What's your name? ")
if name == "Alice" or name == "Bob":
  print("Hello, " + name)
else:
  print("Hello, user")

var_number = input("Give me a number: ")
i = 0
sum_number = 0
while i <= var_number:
  sum_number = sum_number + i
  i += 1
print("The sum of the numbers from 1 to the number you gave me is: ")
print(sum_number)
