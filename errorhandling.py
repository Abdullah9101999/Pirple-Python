x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")

y = -1

if y < 0:
  raise Exception("Sorry, no numbers below zero")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")