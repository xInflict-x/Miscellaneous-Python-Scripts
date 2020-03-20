wordToGuess = input("Player 1: Enter a word.\n> ")

guessed = []
wordInList = []
emptyWord = []
displayText = 6

scene1 = """
  |--------|
  |        |
  |        O
  |       -|-
  |        |
  |       -^-
  |
  |
  """
scene2 = """
  |--------|
  |        |
  |        O
  |        |-
  |        |
  |       -^-
  |
  |
  """
scene3 = """
  |--------|
  |        |
  |        O
  |        |
  |        |
  |       -^-
  |
  |
  """
scene4 = """
  |--------|
  |        |
  |        O
  |        |
  |        |
  |        ^
  |
  |
  """
scene5 = """
  |--------|
  |        |
  |        O
  |        
  |        
  |         
  |
  |
  """
scene6 = """
  |--------|
  |        |
  |        
  |         
  |        
  |         
  |
  |
  """

for x in wordToGuess:
  emptyWord.append("_")

for x in wordToGuess:
  wordInList.append(x)

while True:
  guess = input("Player 2: Guess a letter.\n> ")
  print("\n" * 100)

  if guess in wordInList:

    print("Correct!")

    if guess in wordToGuess:
        for i in range(0, len(wordToGuess)):
            if wordToGuess[i] == guess:
                emptyWord[i] = guess


    if "".join(emptyWord) == wordToGuess:
      print("You win!")
      break

  else:
    print("Incorrect!")

    displayText -= 1

    if displayText == 1:
      print(scene1)
      print("You lose!")
      print("The word was " + wordToGuess)
      break
    if displayText == 2:
      print(scene2)
    if displayText == 3:
      print(scene3)
    if displayText == 4:
      print(scene4)
    if displayText == 5:
      print(scene5)
    if displayText == 6:
      print(scene6)
  guessed.append(guess)
  print(" ".join(emptyWord))
  print("Guessed letters: " + ", ".join(guessed))