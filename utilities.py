import random
import subprocess as sp
def clear():
  print("     " * 10000)
def ipcheck():
  pop3 = input("Enter the IP address: ")
  status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop3))
  if status == 0:
    print("System " + str(pop3) + " is UP !")
  else:
    print("System " + str(pop3) + " is DOWN !")
  menu()
def randomnumgen():
 limit = int(input("What do you want the generator to go to?\n> "))
 print(random.randint(0, limit))
 menu()
workingp = [] 
def ip4gen():
  for x in range(0, 10):
    p1 = str(random.randint(0, 255))
    p2 = str(random.randint(0, 255))
    p3 = str(random.randint(0, 255))
    p4 = str(random.randint(0, 255))
    q1 = str(random.randint(0, 255))
    q2 = str(random.randint(0, 255))
    q3 = str(random.randint(0, 255))
    q4 = str(random.randint(0, 255))
    per = "."
    pop = (p1 + str(per) + p2 + str(per) + p3 + str(per) + p4)
    pop2 = (q1 + str(per) + q2 + str(per) + q3 + str(per) + q4)
    status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop2))
    if status == 0:
      print("System " + str(pop2) + " is UP !")
      print(pop2)
      worked = str(pop2)
      workingp.append(worked)
    else:
      print("System " + str(pop2) + " is DOWN !")
    pop = str()
    status,result = sp.getstatusoutput("ping -c1 -w2 " + str(pop))
    if status == 0:
      print("System " + str(pop) + " is UP !")
      print(pop)
      worked2 = str(pop)
      workingp.append(worked2)
    else:
      print("System " + str(pop) + " is DOWN !")
  ipmenu()
def ipmenu():
  ip_choice = input("1)Generate IP's\n2)View Working IP's\n3)Exit\n> ") 
  if ip_choice == "1":
    ip4gen()
  if ip_choice == "2":
    print(workingp)
    input()
    ipmenu()
  if ip_choice == "3":
    menu()
def utillist():
 util_choice = input("1)Guessing Game\n2)Random Number Generator\n3)Ping\n4)IP Generator\n5)Exit\n> ")
 if util_choice == "1":
   gg()
 if util_choice == "2":
   randomnumgen()
 if util_choice == "3":
   ipcheck()
 if util_choice == "4":
   ipmenu()
 if util_choice == "5":
   menu()
def menu():
 user_input = input("1)Utilities\n2)Info\n3)Exit\n> ")
 if user_input == "1":
   utillist()
 if user_input == "2":
   info()
 if user_input == "3":
   clear()
   exit()
def info():
 print("Created by Jack.")
 input()
 menu()
def gg():
 print("I am holding a number behind my back, can you guess what it is in 3 tries?")
 count = 0
 rn = random.randint(1, 10)
 guess = int(input("> "))
 if guess == rn:
   print("You win!")
 else:
   print("Nope!")
   guess = int(input("> "))
   if guess == rn:
     print("You win!")
   else:
     print("Nope!")
     guess = int(input("> "))
     if guess == rn:
       print("You win!")
     else:
       print("Nope!")
       print("You lose!")
   count = count + 1
 if count == 3:
   print("You lose!")
   print("The number was " + str(rn))
   input()
 menu()
menu()