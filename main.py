import game_data
import random
import art

score = 0
game_on = True
dir = game_data.data

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_guess(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

while game_on:
    random1 = random.choice(dir)
    random2 = random.choice(dir)

    print(art.logo)
    print(f"Compare A: {format_data(random1)}")
    print(art.vs)
    print(f"Against B: {format_data(random2)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    random1_follower_count = random1["follower_count"]
    random2_follower_count = random2["follower_count"]

    is_correct = check_guess(guess,random1_follower_count,random2_follower_count)

    if is_correct:
        score += 1
        print(f"Correct answer! - Current score: {score}")
    else:
        print(f"That's wrong! Final score: {score}")
        game_on = False
        break