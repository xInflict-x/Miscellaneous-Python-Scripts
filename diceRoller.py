import random
import time


diceOne = random.randint(1, 6)
time.sleep(1)
print("You rolled a" , diceOne)

diceTwo = random.randint(1, 6)
time.sleep(1)
print("You rolled a" , diceTwo)

time.sleep(1)
if diceOne == diceTwo:
  print("You win!")
else:
  print("You lose.")