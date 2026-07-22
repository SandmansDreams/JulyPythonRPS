# 1. Have computer make a choice
# 2. Have the user input a choice
# 3. Verify user input
# 4. Compare choices and determine winner
# 5. Print results

# 1 = rock | 1 beats 3
# 2 = paper | 2 beats 1
# 3 = scissors | 3 beats 2

import random

# Helpers
def convertToPlay(number: int) -> str: # Converts an int back into a string representing the play
    if number == 1: 
        return "Rock"
    elif number == 2: 
        return "Paper"
    elif number == 3:
        return "Scissors"
    else:
        return "Unreadable"

def compare(a, b) -> int: # Compare two ints to determine a winner
    if a == b:
        return 0
    elif a == 1 and b == 3: 
        return 1
    elif a == 2 and b == 1: 
        return 1 
    elif a == 3 and b == 2: 
        return 1
    else:
        return 2

# Main
def main():
    computerChoice = random.randint(0, 2) # Get random choice
    userChoice = input("Rock, paper, or scisors?: ").lower()

    def convertToNumber(string: str) -> int:
        choice = string.strip()

        if choice == "rock" or choice == "r" or choice == "1":
            return 1
        elif choice == "paper" or choice == "p" or choice == "2":
            return 2
        elif choice == "scissors" or choice == "s" or choice == "3":
            return 3
        else:
            print("Sorry, that didn't make any sense...")
            return 0


    converted = convertToNumber(userChoice)
    condition = compare(converted, computerChoice)

    userPlay = convertToPlay(converted)
    computerPlay = convertToPlay(computerChoice)

    print("Computer Choice: " + computerPlay)
    print("Player Choice: " + userPlay)

    if condition == 1:
        print("Player has won! " + userPlay + " beats " + computerPlay)
    elif condition == 0:
        print("It's a Tie! " + computerPlay + " ties with " + userPlay)
    elif condition == 2:
        print("Computer has won! " + computerPlay + " beats " + userPlay)

main()
