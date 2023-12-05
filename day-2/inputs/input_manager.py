def load_inputs(input_filename: str = "./inputs/input.txt"):
    """returns a list containing all the strings specified in the input.txt"""
    list_to_return = []

    with open(f"{input_filename}", "r") as file:
        lines = file.readlines()
        for line in lines:
            # get rid of the newline character at the end of each line
            line_to_append = line.split("\n")[0]
            list_to_return.append(line_to_append)

        file.close()

    return list_to_return
