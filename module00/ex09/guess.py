from random import randint, seed
from random import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit'to end the game.")
print("Good luck")

while 1:
    print("What's your guess between 1 and 99?")
    u_in = input(">>>")
    if u_in == "exit" or not u_in.isdigit():
        print("Goodbye")
        break
    elif int(u_in) > 42:
        print("Too high!")
    elif int(u_in) < 42:
        print("Too low!")
    else:
        print("The answer to the ultimate question of life, the universe and everything is 42.")
        print("Congratulations! You got it on your first try!")
        break