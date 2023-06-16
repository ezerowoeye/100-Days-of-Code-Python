import random
from game_data import data
from art import logo, vs
# from replit import clear
# Only works in replit

choice = ""
choice2 = ""
first = ""
second = ""

def printchoice(choice, choice2):
#   clear()
  print(logo)
  print(f"Compare A: {choice['name']} , a {choice['description']}, from {choice['country']}.")
  print(vs)
  print(f"Against B: {choice2['name']} , a {choice2['description']}, from {choice2['country']}.")

is_true = True
def game(first, second, choice, choice2):
  is_true = True
  while is_true:
    play_again = input("Do you want to play? y or n: ").lower()
    # clear()
    if play_again == 'y': 
      choice = random.choice(data)
      choice2 = random.choice(data)
      first = choice['follower_count']
      second = choice2['follower_count']
      printchoice(choice, choice2)
      current_score = 0

      secondtime = True
      while secondtime:
        # print(first)
        # print(second)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
 
        if answer == "a"  and first > second:
          current_score += 1
          print("entered A")
          print(f"You're right! Current score: {current_score}.")
          choice = choice2
          choice2 = random.choice(data)
          if choice == choice2:
            choice2 = random.choice(data)
          first = choice['follower_count']
          second = choice2['follower_count']   
          printchoice(choice, choice2)
        elif answer == "b" and second > first:
          current_score += 1
          print("entered B \n")
          print(f"You're right! Current score: {current_score}.")
          choice = choice2
          choice2 = random.choice(data)
          if choice == choice2:
            choice2 = random.choice(data)
          first = choice['follower_count']
          second = choice2['follower_count']
          printchoice(choice, choice2)
        else:
        #   clear()
          print(logo)
          print(f"Sorry, well, that's wrong. Final score: {current_score}.")
          secondtime = False
  
    else:
      is_true = False

game(first, second, choice, choice2)