import random
from art import logo
from art import vs
from game_data import data
def gamer(acc):
    acc_name=acc["name"]
    acc_des=acc["description"]
    acc_country=acc["country"]
    return f"{acc_name}, a {acc_des},from {acc_country}"
def check_answer(user_input,followers_count1,followers_count2):
    if followers_count1>followers_count2:
        return user_input=="a"
    else:
        return user_input=="b"
score=0
initial=True
acc2 = random.choice(data)
while initial:
    acc1 = acc2
    acc2 = random.choice(data)
    if acc1 == acc2:
        acc2 = random.choice(data)
    print(logo)
    print(f"Compare A: {gamer(acc1)}")
    print(vs)
    print(f"Compare B: {gamer(acc2)}")
    user_input=input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 20)
    print(logo)
    followers_count1 = acc1["follower_count"]
    followers_count2 = acc2["follower_count"]
    is_correct = check_answer(user_input, followers_count1, followers_count2)
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        initial = False