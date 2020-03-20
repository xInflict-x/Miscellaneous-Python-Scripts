import random
import time

global char_hp
global enemy_hp
global wins
global loses

char_hp = 100
enemy_hp = 100
wins = 0
loses = 0

def clear():
  print("\n" * 250)

def s_menu():
  global char_hp, enemy_hp, wins, loses
  char_hp = 100
  enemy_hp = 100
  print("1)Start\n2)W/L Ratio\n3)Info\n4)Exit")
  user_choice = input("\n")
  if user_choice == "1":
    clear()
    start()
  if user_choice == "2":
    clear()
    print("You have " + str(wins) + " wins and " + str(loses) + " loses.")
    s_menu()
  if user_choice == "3":
    clear()
    info()
    s_menu()
  if user_choice == "4":
    clear()
    exit()
  else:
    s_menu()

def info():
  print("Created by Jack.")
  s_menu()

def backup():
  chance = random.randint(0, 2)
  clear()
  if chance == 1:
    d_you()
  if chance == 2:
    d_them()
  else:
    backup()

def start():
  global char_hp, enemy_hp, wins, loses
  if char_hp <= 0:
    print("You lose!")
    loses += 1
    s_menu()
  if enemy_hp <= 0:
    print("You win!")
    wins += 1
    s_menu()
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  time.sleep(1)
  print("...Fight!")
  chance = random.randint(0, 2)
  clear()
  if chance == 1:
    d_you()
  if chance == 2:
    d_them()
  else:
    backup()

def d_you():
  global enemy_hp, char_hp, wins, loses
  d_chance = random.randint(0, 6)
  if d_chance == 1:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("You did 10 damage!\n")
    print("Enemy HP: " + str(enemy_hp - 10))
    enemy_hp = enemy_hp - 10
    start()
  if d_chance == 2:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("You did 20 damage!\n")
    print("Enemy HP: " + str(enemy_hp - 20))
    enemy_hp = enemy_hp - 20
    start()
  if d_chance == 3:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("You did 30 damage!\n")
    print("Enemy HP: " + str(enemy_hp - 30))
    enemy_hp = enemy_hp - 30
    start()
  if d_chance == 4:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("You tried to attack, but you missed!\n")
    print("Enemy HP: " + str(enemy_hp))
    start()
  if d_chance == 5:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("You tried to attack, but you missed! He counter attacked you for 10 damage!\n")
    print("Your HP: " + str(char_hp - 10))
    char_hp = char_hp - 10
    start()
  if d_chance == 6:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("You tried to attack, but you missed! He counter attacked you for 20 damage!\n")
    print("Your HP: " + str(char_hp - 20))
    char_hp = char_hp - 20
    start()
  else:
    print("You both clashed swords, backing off.")
    start()

def d_them():
  global enemy_hp, char_hp, wins, loses
  if char_hp <= 0:
    print("You lose!")
    loses += 1
    s_menu()
  if enemy_hp <= 0:
    print("You win!")
    wins += 1
    s_menu()
  d_chance = random.randint(0, 6)
  if d_chance == 1:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("The enemy did 10 damage!\n")
    print("Your HP: " + str(char_hp - 10))
    char_hp = char_hp - 10
    start()
  if d_chance == 2:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("The enemy did 20 damage!\n")
    print("Your HP: " + str(char_hp - 20))
    char_hp = char_hp - 20
    start()
  if d_chance == 3:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("The enemy did 30 damage!\n")
    print("Your HP: " + str(char_hp - 30))
    char_hp = char_hp - 30
    start()
  if d_chance == 4:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("The enemy tried to attack, but he missed!\n")
    print("Your HP: " + str(char_hp))
    start()
  if d_chance == 5:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("He tried to attack, but he missed! You counter attacked for 10 damage!\n")
    print("Enemy HP: " + str(enemy_hp - 10))
    enemy_hp = enemy_hp - 10
    start()
  if d_chance == 6:
    if enemy_hp <= 0:
      print("You win!")
      wins = wins + 1
      s_menu()
    if char_hp <= 0:
      print("You lose.")
      loses = loses + 1
      s_menu()
    print("He tried to attack, but he missed! You counter attacked for 20 damage!\n")
    print("Enemy HP: " + str(enemy_hp - 20))
    enemy_hp = enemy_hp - 20
    start()
  else:
    print("You both clashed swords, backing off.")
    start()
s_menu()