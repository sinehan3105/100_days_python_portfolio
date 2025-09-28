import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
choosen_number=random.randint(1,100)
def game():
    attempts = True
    while attempts:
        global n
        print(f"you have {n} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > choosen_number:
            print("Too high.")
        elif user_guess<choosen_number:
            print("Too low")
        elif user_guess==choosen_number:
            print("Congratulation You Won The Game")
            break
        n=n-1
        if n>0:
            print("Guess Again....\n")
        if n==0:
            attempts= False
            print("You've run out of guesses. Refresh the page to run again.")
            print(f"The correct number is {choosen_number}.")

if level=="hard":
    n=5
    game()
else:
    n=10
    game()
