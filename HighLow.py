import random
import sys
from gamedata import game_data,logo,vs

print(logo)

#Initialisung variables
dict1={}
dict2={}
score = 0
game_end = 0

#Initialising dicionaries and storing data
dict1 = random.choice(game_data)
winnerdict = dict1 #Initialising winnerdict

while game_end == 0:
    # Ensure dict2 is not the same as winnerdict
    while True:
        dict2 = random.choice(game_data)
        if dict2['Name'] != winnerdict['Name']:
            break

    # Taking user input
    print(f"Compare A: {winnerdict['Name']}, a {winnerdict['Description']}, from {winnerdict['Country']}")
    print(vs)
    print(f"Against B: {dict2['Name']}, a {dict2['Description']}, from {dict2['Country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    # Comparison between followers
    if choice == 'A':
        if winnerdict['FollowerCount'] > dict2['FollowerCount']:
            print(f"Correct choice!! {winnerdict['Name']} has the most follower count.")
            score += 1
            # winnerdict remains the same
        else:
            print("Incorrect Choice, Game Over!!")
            game_end = 1
    elif choice == 'B':
        if dict2['FollowerCount'] > winnerdict['FollowerCount']:
            print(f"Correct choice!! {dict2['Name']} has the most follower count.")
            score += 1
            winnerdict = dict2
        else:
            print("Incorrect Choice, Game Over!!")
            game_end = 1
    else:
        print("Invalid Input!")

print(f"Your score = {score}")
