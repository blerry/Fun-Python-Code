import random
import math
max = int(input("Enter the maximum number: "))
max_guesses = math.ceil(math.log(max,2))
target = random.randint(1,max)
num_guesses = 1

while True:
  if num_guesses > max_guesses:
    print ("Sorry, you lost")
    break
  guess = int(input("Guess a number between 1 and " + str(max) + ": "))
  num_guesses += 1
  if guess == target:
    print ("You got it!!")
    break
  elif guess < target:
    print ("Sorry, too low -- try a higher number")
  elif guess > target:
    print ("Sorry, too high -- try a lower number")
