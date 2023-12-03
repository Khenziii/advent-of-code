def load_inputs(input_filename: str = "./input.txt"):
    """returns a list containing all of the strings specified in the input.txt"""
    list_to_return = []

    with open(f"{input_filename}", "r") as file:
        lines = file.readlines()
        for line in lines:
            # get rid of the newline character at the end of each line
            line_to_append = line.split("\n")[0]
            list_to_return.append(line_to_append)
        
        file.close()
    
    return list_to_return

def calculate_value_for_line(line: str):
    value = ""

    for char in line:
        # try to convert it into a integer
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


input_list = load_inputs()
value_list = []

for input_string in input_list:
    value_list.append(calculate_value_for_line(input_string))

print(f"answer: {sum(value_list)}")
