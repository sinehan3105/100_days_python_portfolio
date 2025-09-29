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
user_choice=int(input("Select your choice:- rock for '0',paper for '1',scissors for '2'----->"))
print(f"Your choice is : {user_choice}\n")
handsign=[rock,paper,scissors]
if user_choice >= 0 and user_choice <= 2:
    print(handsign[user_choice])
computerchoice=random.randint(0, 2)
print(f"The Computer choice is : {computerchoice}")
print(handsign[computerchoice])
if user_choice=="0" and computerchoice=="2":
    print("You win!")
elif user_choice=="1" and computerchoice=="0":
    print("You win!")
elif user_choice=="2" and computerchoice=="1":
    print("You win!")
elif user_choice==computerchoice:
    print("Draw")
else:
    print("You lose")