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

#Write your code below this line 👇
import random
user_choice = input('What do yo choice? 0 for rock, 1 for paper, 2 for scissors ')
user_choice = int(user_choice)
print(f"user Choice {user_choice}")

computer_choice = random.randint(0,2)
computer_choice = int(computer_choice)
print(f'Computer choose {computer_choice}')


if user_choice == 0 or computer_choice == 0:
  print('user choice is rock and computer choice is also rock')
  print("User Chocie"+rock)
  print("Computer Choice"+rock)
  print('Match Draw')

elif user_choice == 0 or computer_choice == 1:
  print('user choice is rock and computer choice is paper')
  print("User Chocie"+rock)
  print("computer Choice"+paper)
  print('Computer Won!')
  
elif user_choice == 0 or computer_choice == 2:
  print('user choice is rock and computer choice is scissors')
  print('user choice'+ rock)
  print('computer choice'+scissors)
  print('You Won')

elif computer_choice == 0 or user_choice == 0:
  print('computer choice is rock and user choice is rock')
  print('computer choice'+ rock)
  print('user choice'+rock)
  print('Match Draw')

elif computer_choice == 0 or user_choice == 1:
  print('computer choice is rock and user choice is paper')
  print('computer choice'+ rock)
  print('user choice'+paper)
  print('You won')
  
elif computer_choice == 0 and user_choice == 2:
  print('computer choice is rock and user choice is scissors')
  print('computer choice'+ rock)
  print('user choice'+scissors)
  print('Computer won')

else:
  print('restart')
