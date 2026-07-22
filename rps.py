# 1. Have computer make a choice
# 2. Have the user input a choice
# 3. Verify user input
# 4. Compare choices and determine winner
# 5. Print results

# 1 = rock | 1 beats 3
# 2 = paper | 2 beats 1
# 3 = scissors | 3 beats 2

import random

computerChoice = random.randint(1, 3) # Get random choice
userChoice = input("Rock, paper, or scisors?: ")

print("Computer Choice: ")
print(computerChoice)
print("Player Choice: ")
print(userChoice)