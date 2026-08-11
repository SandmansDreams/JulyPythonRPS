""" REQUIREMENTS
- Take user input
- Perform appropriate operations (EMDAS)
- Return solution
- Try to be bugless, or catch bugs before a crash

Potential math:
1 + 1
4 - 6
1 / 0
5 * 20
5+10-11*7^2
(5 - 10)^2 - 10 / 3 + 12
(5 - 10)^3 - (5 + 10)^4
"""

""" IMPORTS """
import math

""" HELPER FUNCTIONS """
# Take in list of nums so the operation can be done on any amount of numbers
def add(nums):
    return sum(nums)

def subtract(nums): # Ignored
    subtracted = nums[0]

    for num in nums[1:]:
        subtracted -= num

    return subtracted

def multiply(nums):
    return math.prod(nums)

def divide(nums):
    if nums[0] == 0: # Zero divided by anything is zero
        return 0

    # Attempt division
    try: 
        divided = nums[0]
        
        for num in nums[1:]:
            divided /= num

        return divided
    except ZeroDivisionError: # Can't divide by zero
        raise ZeroDivisionError("Cannot divide by zero")

def exponentiate(nums): # Would be better to have 2 inputs but should match the rest
    """ # Handle 0 case, number to power zero is always 1
        if exponent == 0:
            return 1
        
        # Get the proper base number
        nums = [base] * abs(exponent)
        result = multiply(nums)

        # Handle negative exponents
        if exponent < 0:
            return 1 / result
        else:
            return result
    """

    # Did all that ^ and then realized:
    return nums[0] ** nums[1]

def convert_floats(equation): # Replace all valid floats with floats
    converted = []

    for value in equation:
        try:
            converted.append(float(value))
        except ValueError:
            converted.append(value)

    return converted

def convert_from_words(equation):
    converted = []
    
    for value in equation:
        if value in numberMap:
            converted.append(numberMap[value])
            continue

        if value in operatorMap:
            converted.append(operatorMap[value])
            continue

        converted.append(value)

    return converted

def handle_math(equation, operator, operation): # Operates on the provided list
    print(f"Handling math of '{operator}' operator")
    index = 0

    # Special case for exponents
    if operator == "^":
        # Reverse index for exponents, other orders don't matter
        reversed = equation[::-1] # Reverse the list
        r_ind = reversed.index(operator)
        index = len(equation) - 1 - r_ind
    else:
        # Gets indexes of operator in list
        try: 
            index = equation.index(operator)
        except ValueError:
            print(f"No more indexes of {operator}. Skipping.")
            return

    # Get values of surrounding stuff
    prev_index = index - 1
    next_index = index + 1
    prev_value = equation[prev_index]
    next_value = equation[next_index]

    print(f"Performing {prev_value} {operator} {next_value} at index {index}")

    # Run the proper operation on the values
    result = operation([prev_value, next_value])

    # Replace indexes with result
    equation[prev_index:next_index + 1] = [result]

    print(f"Handle result: {result}. Replaced indexes {prev_index} - {next_index}")

def iterate(equation) -> int: # Iterate through EMDAS and perform in-place replacements for the math
    for key, value in operations.items():
        while key in equation:
            # Special case for subtraction (or else order is messed up)
            if key == "-":
                print("Handling subtraction by swapping all minus signs to adding a negative value")
                negative_indexes = [i for i, val in enumerate(equation) if val == key]

                while len(negative_indexes) > 0:
                    # Get last index and swap its sign, then make the next float negative
                    index = negative_indexes.pop()
                    equation[index] = "+"
                    equation[index + 1] = -equation[index + 1]

                print(f"Equation is now: {' '.join(str(num) for num in equation)}")

            # Special case for addition (for greater optimization), the final return
            elif key == "+": 
                # By this point, the only operators left should be "+"
                print("Handling addition (final step)")
                equation = [i for i in equation if i != "+"] # Remove pluses

            else:
                handle_math(equation, key, value)
                print(f"Equation is now: {' '.join(str(num) for num in equation)}")

    return add(equation) # Sum it all

""" DECLARATIONS """
operations = { # Order is important
    "^": exponentiate,
    "*": multiply,
    "/": divide,
    "-": subtract,
    "+": add,
}

operatorMap = {
    # Addition
    "plus": "+",
    "add": "+",

    # Subtraction
    "minus": "-",
    "subtract": "-",

    # Multiplication
    "times": "*",
    "multiplied": "*",
    "x": "*",

    # Division
    "divided": "/",
    "divide": "/",
    "over": "/",

    # Parentheses
    "open": "(",
    "close": ")",
}

numberMap = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "twenty-one": 21,
    "twenty-two": 22,
    "twenty-three": 23,
    "twenty-four": 24,
    "twenty-five": 25,
    "twenty-six": 26,
    "twenty-seven": 27,
    "twenty-eight": 28,
    "twenty-nine": 29,
    "thirty": 30,
    "thirty-one": 31,
    "thirty-two": 32,
    "thirty-three": 33,
    "thirty-four": 34,
    "thirty-five": 35,
    "thirty-six": 36,
    "thirty-seven": 37,
    "thirty-eight": 38,
    "thirty-nine": 39,
    "forty": 40,
    "forty-one": 41,
    "forty-two": 42,
    "forty-three": 43,
    "forty-four": 44,
    "forty-five": 45,
    "forty-six": 46,
    "forty-seven": 47,
    "forty-eight": 48,
    "forty-nine": 49,
    "fifty": 50,
    "fifty-one": 51,
    "fifty-two": 52,
    "fifty-three": 53,
    "fifty-four": 54,
    "fifty-five": 55,
    "fifty-six": 56,
    "fifty-seven": 57,
    "fifty-eight": 58,
    "fifty-nine": 59,
    "sixty": 60,
    "sixty-one": 61,
    "sixty-two": 62,
    "sixty-three": 63,
    "sixty-four": 64,
    "sixty-five": 65,
    "sixty-six": 66,
    "sixty-seven": 67,
    "sixty-eight": 68,
    "sixty-nine": 69,
    "seventy": 70,
    "seventy-one": 71,
    "seventy-two": 72,
    "seventy-three": 73,
    "seventy-four": 74,
    "seventy-five": 75,
    "seventy-six": 76,
    "seventy-seven": 77,
    "seventy-eight": 78,
    "seventy-nine": 79,
    "eighty": 80,
    "eighty-one": 81,
    "eighty-two": 82,
    "eighty-three": 83,
    "eighty-four": 84,
    "eighty-five": 85,
    "eighty-six": 86,
    "eighty-seven": 87,
    "eighty-eight": 88,
    "eighty-nine": 89,
    "ninety": 90,
    "ninety-one": 91,
    "ninety-two": 92,
    "ninety-three": 93,
    "ninety-four": 94,
    "ninety-five": 95,
    "ninety-six": 96,
    "ninety-seven": 97,
    "ninety-eight": 98,
    "ninety-nine": 99,
    "one hundred": 100,
}

""" MAIN """
def main():
    isMathing = True
    while isMathing:
        equation_input = input("Type some math: ").lower()
        print(equation_input)

        # Handle exit
        if equation_input in ['quit', 'q', 'exit', 'e', 'end', 'cancel', 'c']:
            isMathing = False
            break

        # Add spaces around operators (if exist)
        for operator in operations.keys(): 
            equation_input = equation_input.replace(operator, f" {operator} ")
        equation_input = equation_input.replace("(", " ( ")
        equation_input = equation_input.replace(")", " ) ")

        equation = equation_input.split() # Split the math by spaces
        print(equation)

        equation = convert_from_words(equation) # Turn words into math
        print(equation)

        equation = convert_floats(equation) # Turn numbers into floats
        print(equation)

        result = 0

        # Handle parenthesees
        print("Handling parenthetical")
        while "(" in equation:
            openIndex = equation.index("(") 
            closeIndex = equation.index(")")

            inner = equation[openIndex + 1:closeIndex] # Clone the inner part

            inner = iterate(inner)

            equation[openIndex:closeIndex + 1] = [inner] # Replace the whole thing with the equated value

        print(f"No more parentheses. Equation is now: {' '.join(str(num) for num in equation)}")

        result = iterate(equation)

        print("")
        print(f"The answer is: {result}")
            
main()