"""part 2 of this challenge: https://adventofcode.com/2023/day/1"""

from inputs import input_manager
from word2number import w2n as word2nums

def check_if_number_at_index(index: int, string):
    """checks if any number in a string for is at a certain index of another string"""
    for number_as_string in nums_as_string_list:
        if string[index:index + len(number_as_string)] == number_as_string:
            return string[index:index + len(number_as_string)]

    return None


def extract_numbers_from_string(string: str):
    """extracts all ints and ints written in a stringy form from a string"""
    string_to_return = ""

    for i, char in enumerate(string):
        # check if a number's string starts here
        number_as_string = check_if_number_at_index(i, string)
        if number_as_string is not None:
            string_to_return += str(word2nums.word_to_num(number_as_string))
            continue

        try:
            int(char)
            string_to_return += char
        except ValueError:
            ...

    return string_to_return


def calculate_value_for_line(line: str):
    """Calculates a value for a string in the way that is required in the challenge"""
    value = extract_numbers_from_string(line)

    # the numbers need to be 2 chars long
    # if there is only one character, double it
    if len(value) == 1:
        return int(value + value)

    # else return the first and the last number of the string
    return int(value[0] + value[-1])


input_list = input_manager.load_inputs()
nums_as_string_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
value_list = []

for input_string in input_list:
    value_list.append(calculate_value_for_line(input_string))

print(f"answer: {sum(value_list)}")
