import math
import random

player_total = 0
computer_total = 0
round_num = 1

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def calculate_score(d1, d2):
    # Snake eyes
    if d1 == 1 and d2 == 1:
        return 0, "snake"
    # Doubles
    if d1 == d2 and d1 != 1:
        return (d1 + d2) * 2, "double"
    # Normal roll
    return d1 + d2, "normal"

print("Hi there! Welcome to DICE")
print("- To View The Rules, Press 'r'")
print("- To play the game, Press 'p'")
user_response = input(">> ").lower()
if user_response == "r":
    print("DICE RULES:")
    print("This program uses a simplified version of traditional Dice rules.")
    print(" ")
    print("BASIC:")
    print("Each round, you will roll two dice. The goal is to have a higher score than the computer.")
    print("Score is calculated by adding the two dice together and applying any relevant combo effects.")
    print("You can re-roll your dice once per turn if you choose.")
    print(" ")
    print("COMBOS:")
    print("Snake Eyes - Rolling two 1's is an automatic loss.")
    print("Doubles - Rolling two of the same number (except 1) doubles your score.")
    print(" ")
    print("Press 'p' to begin.")
    begin = input(">> ").lower()
    if begin == "p":
        pass
    else:
        pass
elif user_response == "P":
    pass

# Game
playing = True

while playing:
    print(f"\n--- ROUND {round_num} ---")
    input("Press ENTER to roll your dice...")

    # Player
    d1, d2 = roll_dice()
    score, combo = calculate_score(d1, d2)
    print(f"You rolled: {d1} and {d2}")

    if combo == "snake":
        print("SNAKE EYES! Automatic loss this round.")
        player_score = 0
    else:
        player_score = score
        print(f"Your score: {player_score}")

    # Reroll
    reroll = input("Would you like to reroll? (y/n): ").lower()
    if reroll == "y":
        d1, d2 = roll_dice()
        score, combo = calculate_score(d1, d2)

        print(f"You rerolled: {d1} and {d2}")

        if combo == "snake":
            print("SNAKE EYES! Automatic loss this round.")
            player_score = 0
        else:
            player_score = score
            print(f"New score: {player_score}")
    
    # Computer
    cd1, cd2 = roll_dice()
    c_score, c_combo = calculate_score(cd1, cd2)

    print(f"\nComputer rolled: {cd1} and {cd2}")

    if c_combo == "snake":
        print("Computer got Snake Eyes!")
        computer_score = 0
    else:
        computer_score = c_score
        print(f"Computer score: {computer_score}")

    # Compare
    if player_score > computer_score:
        print("You win this round!")
        player_total += 1
    elif computer_score > player_score:
        print("Computer wins this round!")
        computer_total += 1
    else:
        print("It's a tie!")

    print(f"\nTOTAL WINS — You: {player_total} | Computer: {computer_total}")

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        playing = False

    round_num += 1


print("\nThanks for playing!")
