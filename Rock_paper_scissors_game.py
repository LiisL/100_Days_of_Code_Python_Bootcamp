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
rock_paper_scissors=[rock,paper,scissors]

user_selection=int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_selection >= 3 or user_selection < 0: 
  print("You typed an invalid number, you lose!")
else:
    print(f"You chose:{rock_paper_scissors[user_selection]}")
  
    computer_selection = random.randint(0,2)
    print(f"Computer chose: {rock_paper_scissors[computer_selection]}")
  
    if user_selection == 0 and computer_selection == 2:
      print("You win!")
    elif computer_selection == 0 and user_selection == 2:
      print("You lose")
    elif computer_selection > user_selection:
      print("You lose")
    elif user_selection > computer_selection:
      print("You win!")
    elif computer_selection == user_selection:
      print("It's a draw")