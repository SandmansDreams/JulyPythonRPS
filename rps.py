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
def convertToNumber(string: str) -> int: # Convert input to a number
    choice = string.strip()

    if choice in ["rock", "r", "1"]:
        return 1
    elif choice in ["paper", "p", "2"]:
        return 2
    elif choice in ["scissors", "s", "3"]:
        return 3
    elif choice in ["quit", "q", "exit", "e", "4"]:
        return 4
    else: # Should not be possible
        return 0 
    
def compare(a, b) -> int: # Compare two ints to determine a winner
    # Tie
    if a == b:
        return 1
    # Cases where player wins
    elif a == 1 and b == 3: 
        return 2
    elif a == 2 and b == 1: 
        return 2
    elif a == 3 and b == 2: 
        return 2
    # Quit
    elif a == 4:
        return 4
    # Cases where player loses
    else:
        return 3

def convertToPlay(number: int) -> str: # Converts an int back into a string representing the play
    if number == 1: 
        return "Rock"
    elif number == 2: 
        return "Paper"
    elif number == 3:
        return "Scissors"
    elif number == 4:
        return "Quit"
    else: # Should not be posible
        return "Unreadable"

# Main
def main():
    gameon = True

    while gameon:
        print("")
        computerChoice = random.randint(1, 3) # Get random choice
        userChoice = ""

        validChoice = False
        while not validChoice:
            userChoice = input("Rock, paper, or scisors?: ").lower()
            if userChoice in ["rock", "r", "1", "paper", "p", "2", "scissors", "s", "3", "quit", "q", "exit", "e", "4"]:
                validChoice = True
            else:
                print("Sorry that didn't make sense... try again!")

        converted = convertToNumber(userChoice)
        condition = compare(converted, computerChoice)

        userPlay = convertToPlay(converted)
        computerPlay = convertToPlay(computerChoice)

        print("Computer Choice: " + computerPlay)
        print("Player Choice: " + userPlay)

        if condition == 0:
            print("Your input didn't make sense. Computer won!")
        elif condition == 1:
            print("It's a Tie! " + computerPlay + " ties with " + userPlay)
        elif condition == 2:
            print("Player has won! " + userPlay + " beats " + computerPlay)
        elif condition == 3:
            print("Computer has won! " + computerPlay + " beats " + userPlay)
        elif condition == 4:
            gameon = False
            print("")
            print("Thanks for playing!")

main()
