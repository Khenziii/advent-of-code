"""part 1 of this challenge: https://adventofcode.com/2023/day/2"""

from inputs import input_manager
from typing import List, Dict

# color: str, number_of_cubes: int
# Cubes = Dict[str, int]
# id: int, cubes: List[Cubes], possible: bool
# Game = [int, List[Cubes], bool]

def convertStringToGame(string: str):
    """Takes a string in a certain format and returns a game dictionary for it"""
    # get the game id
    id = int(string.split("Game ")[1].split(":")[0])

    # remove the game id section from the string
    string = string.split(":")[1]

    # get the Cubes objects
    cubes_list = []
    for cubes_string in string.split(";"):
        this_cubes_dictionary = {}
        for cubes in cubes_string.split(","):
            number = cubes.split(" ")[1]
            color = cubes.split(" ")[2]

            this_cubes_dictionary[color] = int(number)

        cubes_list.append(this_cubes_dictionary)

    return [id, cubes_list, True]

def markAsImpossible(game_id: int):
    game_list[game_id - 1][2] = False

def markGameAsPossibleIfPossible(game):
    cubes_all = game[1]

    for cubes in cubes_all:
        for color in cubes.keys():
            if cubes[color] > elfs_cubes[color]:
                markAsImpossible(game[0])
                return

def getValue(game):
    if not game[2]:
        return 0

    return game[0]

elfs_cubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}

input_list = input_manager.load_inputs("./inputs/input.txt")
game_list = []
values_list = []

for line in input_list:
    game_list.append(convertStringToGame(line))

for game in game_list:
    markGameAsPossibleIfPossible(game)

for game in game_list:
    values_list.append(getValue(game))

print(f"answer: {sum(values_list)}")
