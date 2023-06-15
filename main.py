import game_data
import random
import art

game_on = True
score = 0
dir = game_data.data

while game_on:
    random1 = random.choice(dir)
    random2 = random.choice(dir)

    print(f"Current score: {score}")
    print(art.logo)
    print(f"Compare A: {random1['name']}, {random1['description']}, from {random1['country']}")
    print(art.vs)
    print(f"Against B: {random2['name']}, {random2['description']}, from {random2['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ")

    if guess == 'A':
        if random1['follower_count'] > random2['follower_count']:
            score += 1
        elif random1['follower_count'] == random2['follower_count']:
            score += 1
        else:
            print(f"Your was was incorrect! Your final score is: {score}")
            break
    elif guess == 'B':
        if random1['follower_count'] > random2['follower_count']:
            print(f"Your was was incorrect! Your final score is: {score}")
            break
        elif random1['follower_count'] < random2['follower_count']:
            score += 1
        else:
            score += 1