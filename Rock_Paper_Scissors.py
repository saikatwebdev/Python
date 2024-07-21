import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
    _______
---'   ____)____
          ______)
          _______) 
         _______)
---.__________)'''

scissors = '''
    _______ 
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

fuck_you = '''
    _____ 
---'   __)_
          _)_____
       __________)
      (____)
---.__(___)
'''

# now we have to take an input from the UserWarning👇

your_turn = int(input("Type 0 for Rock 1 for Paper or 2 for Scissors... :\n"))

# now we have to print the user's choice
if your_turn == 0:
  print(f'You choose Rock {rock}')
elif your_turn == 1:
  print(f'You choose Paper {paper}')
elif your_turn == 2:
  print(f'You choose Scissors {scissors}')
else:
  print(f'You choose {fuck_you}')

# now we have to print the computer's choice
computer_choice = random.randint(0, 2)

if computer_choice == 0:
  print(f'Computer choose Rock {rock}')
elif computer_choice == 1:
  print(f'Computer choose Paper {paper}')
else:
  print(f'You choose Scissors {scissors}')

# now we have to compare the choices

if (your_turn == 0 and computer_choice == 2) or (your_turn == 1
                                                 and computer_choice == 0):
  print("You win")
elif (your_turn == 2 and computer_choice == 1):
  print("YOU WIN")
else:
  print("You lose")
