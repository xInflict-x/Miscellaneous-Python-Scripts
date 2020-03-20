import random

numberToGuess = random.randint(1, 10)
numberOfGuesses = 0
win = False

while not win:

  numberOfGuesses += 1
  guess = int(input("Guess a number between one and ten.\n> "))

  if guess == numberToGuess:
    win = True
    print("You win!\nIt took you" , numberOfGuesses , "guesses." )

  if guess < numberToGuess:
    print("Too low!")

  if guess > numberToGuess:
    print("Too high!")