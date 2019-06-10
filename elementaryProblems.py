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

multi_number = 0
i = 0
while i <= var_number:
  if i % 3 == 0 or i % 5 == 0:
    multi_number = multi_number + i
  i += 1
print("The sum of the numbers from 1 to the number you gave me that are multiples of 3 and 5 is:")
print(multi_number)

a = input("Give me a number: ")
b = input("Give me another number: ")
a_b_sum = a + b
a_b_dif = a - b
print("The sum of those two numbers is:")
print(a_b_sum)
print("The difference of those two numbers is:")
print(a_b_dif)