"""part 1 of this challenge: https://adventofcode.com/2023/day/1"""

from ..utils import input_manager

def calculate_value_for_line(line: str):
    """Calculates a value for a string in the way that is required in the challenge"""
    value = ""

    for char in line:
        # try to convert it into integer
        try:
            char_int = int(char)

            # if we managed to convert it
            # (it's a number)
            # add it as a string to the value
            value += char
        except ValueError:
            # if it's not a number, just ignore it
            ...

    # the numbers need to be 2 chars long

    # if there is only one character, double it   
    if len(value) == 1:
        return int(value + value)

    # else return the first and the last number of the string
    return int(value[0] + value[-1])


input_list = input_manager.load_inputs("./2023/day-1/inputs/input.txt")
value_list = []

for input_string in input_list:
    value_list.append(calculate_value_for_line(input_string))

print(f"answer: {sum(value_list)}")
