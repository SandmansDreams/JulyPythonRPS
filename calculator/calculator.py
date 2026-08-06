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

Not:
2 ^ 2 ^ 2
(5 + 10) ^ 2 - 10 / 3 + 12
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

operations = { # Order is important
    "^": exponentiate,
    "*": multiply,
    "/": divide,
    "-": subtract,
    "+": add,
}

def convert_floats(equation): # Replace all valid floats with floats
    converted = []

    for value in equation:
        try:
            converted.append(float(value))
        except ValueError:
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

""" MAIN """
def main():
    isMathing = True
    while isMathing:
        equation_input = input("Type some math: ")
        print(equation_input)

        # Handle exit
        if equation_input.lower() in ['quit', 'q', 'exit', 'e', 'cancel', 'c']:
            isMathing = False
            break

        # Add spaces around operators
        for operator in operations.keys(): 
            equation_input = equation_input.replace(operator, f" {operator} ")

        equation = equation_input.split() # Split the math by spaces
        equation = convert_floats(equation)
        print(equation)

        result = 0

        # Iterate through EMDAS and perform in-place replacements for the math
        for key, value in operations.items():
            while key in equation:
                if key == "-": # Special case for subtraction (or else order is messed up)
                    print("Handling subtraction by swapping all minus signs to adding a negative value")
                    negative_indexes = [i for i, val in enumerate(equation) if val == key]

                    while len(negative_indexes) > 0:
                        # Get last index and swap its sign, then make the next float negative
                        index = negative_indexes.pop()
                        equation[index] = "+"
                        equation[index + 1] = -equation[index + 1]

                    print(f"Equation is now: {' '.join(str(num) for num in equation)}")
                elif key == "+": # Special case for addition (for greater optimization)
                    # By this point, the only operators left should be "+"
                    equation = [i for i in equation if i != "+"] # Remove pluses
                    result = add(equation)
                else:
                    handle_math(equation, key, value)
                    print(f"Equation is now: {' '.join(str(num) for num in equation)}")

        print("")
        print(f"The answer is: {result}")
            
main()