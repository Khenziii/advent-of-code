"""part 2 of this challenge: https://adventofcode.com/2023/day/2"""

from inputs import input_manager

def convertStringToGame(string: str):
    """Takes a string in a certain format and returns a game list for it"""
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

    return [id, cubes_list]

def findLowest(game):
    cubes_all = game[1]
    cubes_lowest = {
        "red": -1,
        "green": -1,
        "blue": -1
    }

    for cubes in cubes_all:
        for color in cubes.keys():
            if cubes[color] > cubes_lowest[color]:
                cubes_lowest[color] = cubes[color]

    game_list[game[0] - 1].append(cubes_lowest)

def getValue(game):
    values = game[2]
    int_to_return = 1
    for key in values.keys():
        int_to_return *= values[key]

    return int_to_return


input_list = input_manager.load_inputs("./inputs/input.txt")
game_list = []
values_list = []

for line in input_list:
    game_list.append(convertStringToGame(line))

for game in game_list:
    findLowest(game)

for game in game_list:
    values_list.append(getValue(game))

print(f"answer: {sum(values_list)}")
