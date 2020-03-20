userChoice = input("1)Abs\n2)Bin\n3)Hex\n4)Len\n5)Round\n> ")

if userChoice == "1":
  print(abs(int(input("Enter a number.\n> "))))

if userChoice == "2":
  print(bin(int(input("Enter a number.\n> "))))

if userChoice == "3":
  print(hex(int(input("Enter a number.\n> "))))

if userChoice == "4":
  print(len(input("Enter a string.\n> ")))

if userChoice == "5":
  print(round(float(input("Enter a number.\n> "))))