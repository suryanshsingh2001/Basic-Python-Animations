import os
import time
from random import randint

die = ["   \n O \n   "]  # 1
die.append("  O\n   \nO  ")  # 2
die.append("O  \n O \n  O")  # 3
die.append("O O\n   \nO O")  # 4
die.append("O O\n O \nO O")  # 5
die.append("O O\nO O\nO O")  # 6

#For animation of the die
def animate_die():
    for roll in range(0, 15):
        os.system('cls')
        print("\n")
        number = randint(0, 5)
        print(die[number])
        time.sleep(0.2)
#For animation of the rocket
def animate_rocket():
    distance_from_top = 20
    while True:
        print("\n" * distance_from_top)
        print("          /\        ")
        print("          ||        ")
        print("          ||        ")
        print("         /||\        ")
        time.sleep(0.2)
        os.system('cls')
        distance_from_top -= 1
        if distance_from_top < 0:
            distance_from_top = 20



# Main Program Starts Here....
animate_die()







