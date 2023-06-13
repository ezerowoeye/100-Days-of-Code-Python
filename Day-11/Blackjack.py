import random

the_beginning = True
while the_beginning:
  start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if start == "y":
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    computer_choice = []
    user_choice = []
    
    def result():
      print(f"Your cards: {user_choice}, current score: {user_result}")
      computer_first = computer_choice[0]
      print(f"Computer's first card: {computer_first}")
    
    def computer_guess(card):
      computer_total = 0
      run_through = [0,1]
      for running in run_through:
        computer= random.choice(cards)
        computer_choice.append(computer)

        computer_total += computer_choice[running]
      return computer_total

    def user_guess(cards):
      user_total = 0 

      run_through = [0,1]
      for running in run_through:
        user_pick = random.choice(cards)
        user_choice.append(user_pick)
      
        user_total += user_choice[running]
    
      return user_total
      
    user_result = user_guess(cards)
    computer_result = computer_guess(cards)
    
    result()
      
    is_true = True
    while is_true:
      should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if should_continue == "n":
        is_true = False
      elif should_continue == "y":
        user_pick = random.choice(cards)
        user_choice.append(user_pick)
        # print(user_choice)
        user_index = user_choice.index(user_pick)
        user_result += user_choice[user_index]
  
        if user_result <= 20:
          if computer_result <= 20:
            computer= random.choice(cards)
            computer_choice.append(computer)
          
            computer_index = computer_choice.index(computer)
            computer_result += computer_choice[computer_index]
          result()
        elif user_result > 21:
          is_true = False
      is_comp_again = True
      while is_comp_again:
        if computer_result <= 18:
          computer_answer = ["y", "y", "y", "n"]
          computer_again = random.choice(computer_answer)

          index1 = computer_answer.index(computer_again)

          print(f"this is computer again = {computer_again}")
          if computer_again == "y":
            computer= random.choice(cards)
            computer_choice.append(computer)
          
            computer_index = computer_choice.index(computer)
            computer_result += computer_choice[computer_index]
          else:
            computer_result = computer_result
            is_comp_again = False          
        else:
          is_comp_again= False
        
      
    result()

  print(f"Your final hand: {user_choice}, final score: {user_result}")
  print(f"Computer's final hand: {computer_choice}, final score: {computer_result}")
  # print(f"User result = {user_result}, Computer result = {computer_result}")
  if computer_result == 21 and user_result != 21:
    print("The computer has a blackjack, You lose")
  elif user_result == 21 and computer_result != 21:
    print("You have blackjack, You Win")
  elif user_result > computer_result and user_result < 21:
    print("You Win!")
  elif computer_result > user_result and computer_result < 21:
    print("You lose.")  
  elif user_result > 21 and computer_result > user_result:
    print("Computer went over. You win")
  elif computer_result > 21 and user_result > computer_result:
    print("You went over. You lose")
  elif user_result < 21 and computer_result > 21:
    print("Computer went over. You win")
  elif computer_result < 21 and user_result > 21:
    print("You went over. You lose")
  else:
    print("You Draw")