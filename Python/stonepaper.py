import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]

user_choice = int(input("what do you choose? type 0 for rock, 1 for paper,2 for scissors\n"))
if user_choice >=3 and user_choice < 0:
  print("you typed invaild number, you lose")
else:
  print(game_images[user_choice])
  
  computer_choice = random.randint(0, 2)
  print("computer choice: ")
  print(game_images[computer_choice])
  
  
  if computer_choice == 0 and user_choice == 2:
    print("you loose")
  elif computer_choice == 2 and user_choice ==0:
    print("you win")
  elif computer_choice >  user_choice :
    print("you loose")
  elif computer_choice < user_choice:
    print("you win")
  elif computer_choice == user_choice:
    print("it's a draw")

