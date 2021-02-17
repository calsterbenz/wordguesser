#Hangman Program
#Computers and Technology Programming Final
import random

words = ["house", "cars", "family", "stack", "python", "friend", "programming", "apple", "plane", "blueberry", "coffee", "control", "hangman", "final", "project", "taste", "food", "world", "challenge", "difficult", "launch", "grow", "white", "water", "taste", "smell"]
play = True

print("Welcome to the word guessing game! The rules are simple,\nyou get six tries to guess a word by entering in characters.\nHave the word? Type it in if you think you know it, but be careful as it will count against you. Also, you only get one guess at the word.\n")

while(play):
  word = random.choice(words)
  blank = ""
  letterMem = ""
  countDown = 6
  i = 0

  #Creates a value that contains a '*' for every character in the word.
  for char in word:
    blank += "*"
  
  #Prints the beginning of the game
  print("\nAre you ready to play? You better be.\nYour word is " + blank + ".")

  #While loop runs 6 times to simulate a hangman
  while(i < 6):
    if(i >= 1):
      print("Letters Used: " + letterMem)
    
    print("Guess a letter or the word. " + str(countDown) + " guesses left.")
    uIn = input()

    while(uIn in letterMem):
      print("\nYou have already tried that letter, try again.")
      uIn = input()
    letterMem += uIn + " "

    #Checks if word was guessed right
    if(uIn == word):
      print("\nYou gueesed right! You win!")
      break
    elif(len(uIn) > 1):
      print("\nThat was not the word. You lose! The word was " + word + ".")
      break
    
    #Checks if the users character they guessed is in the word and looks for repeat letters and replaces them in the correct index
    charPos = 0
    timesFound = 0
    if(uIn in word):
      for x in word:
        if(x == uIn):
          blank = blank[:charPos] + x + blank[charPos+1:]
          timesFound += 1
        charPos += 1
      print("\nCorrect! " + uIn.upper() + " was in the word " + str(timesFound) + " time(s).\nYour word is now " + blank + ".")
    elif(i < 5):
      print("\nThe letter, " + uIn.upper() + ", is not in the word, try again")
    i += 1
    countDown -= 1

    if(i == 6):
      print("\nYou ran out of guesses! You lost. :( The word was " + word.upper() + ".")
    elif('*' not in blank):
      print("\nYou have won by filling in all the blanks! Congrats!")
      break

  #End of loop condition
  print("Would you like to play again? y for YES, and n for NO")
  playCon = input()
  if(playCon == 'y'):
    play = True
  else:
    print("\nThanks for playing! Hope to see you soon!")
    break
