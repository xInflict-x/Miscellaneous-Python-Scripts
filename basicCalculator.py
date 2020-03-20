firstNumber = float(input("Enter your first number.\n> "))
secondNumber = float(input("Enter your second number.\n> "))
operation = input("Enter your operation. (A/S/D/M).\n> ")

if operation.upper() == "A":
  print(firstNumber + secondNumber)

if operation.upper() == "S":
  print(firstNumber - secondNumber)

if operation.upper() == "D":
  print(firstNumber / secondNumber)

if operation.upper() == "M":
  print(firstNumber * secondNumber)