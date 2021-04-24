import art
from art import *
from data import data
import random as rn

print(higher_or_lower)

cont = True
A = rn.choice(data)

Score = 0

while cont ==True:

    B = rn.choice(data)




    print(f"{A['name']} who is a {A['description']} from {A['country']} \n")
    print(art.vs)
    print(f"{B['name']} who is a {B['description']} from {B['country']} \n")
    guess = input(f"Does {A['name']} or {B['name']} have more followers? \n")
    more_followers = ""
    if A['follower_count'] > B['follower_count']:
        more_followers = A['name']
    else:
        more_followers = B['name']


    if guess == more_followers:
        print("Correct! \n")
        A = B
        Score += 1
    else:
        print("Incorrect, game over")
        print(f"Your score is {Score}")
        cont = False
