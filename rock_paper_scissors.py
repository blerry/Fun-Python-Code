
import random
player_score = 0
comp_score = 0
while True:
   comp_choice = random.choice(["rock", "paper", "scissors"])
   player_choice = input("Enter rock, paper or scissors, or enter ‘quit’ to exit.")
   if player_choice == "quit":
      break
   elif player_choice == comp_choice:
      print ("You tied")
   elif player_choice == "rock" and comp_choice == "paper":
      print ("you lost")
      comp_score += 1
   elif player_choice == "rock" and comp_choice == "scissors":
      print ("you won")
      player_score += 1
   elif player_choice == "paper" and comp_choice == "rock":
      print ("you won")
      player_score += 1
   elif player_choice == "paper" and comp_choice == "scissors":
      print ("you lost")
      comp_score += 1
   elif player_choice == "scissors" and comp_choice == "paper":
     print ("you won")
     player_score += 1
   elif player_choice == "scissors" and comp_choice =="rock":
    print ("you lost")
    comp_score += 1
   else:
     print ("invalid input -- try again")
print ("The final score is:")
print ("  Computer: " + str(comp_score))
print ("  Player: " + str(player_score))
if player_score == comp_score:
   print ("It's a tie")
elif player_score > comp_score:
   print ("You are the winner -- humans rule!!")
elif player_score < comp_score:
   print ("You are the loser -- computers rule!!!")