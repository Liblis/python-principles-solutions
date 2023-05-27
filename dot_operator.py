# This module inserts dots between each character in a given string.
def add_dots_solution_one(string_input):
    list_input = [character for character in string_input]
    return ".".join(list_input)


def remove_dots_solution_one(string_input):
    return string_input.replace(".", "")


def add_dots_solution_two(string_input):
    output_string = ""

    for character in string_input:
        output_string += character + "."

    return output_string[:-1]


def remove_dots_solution_two(string_input):
    string_output = ""

    for character in string_input:
        if character != ".":
            string_output += character

    return string_output


def add_dots_solution_three(string_input):
    return ".".join(string_input)


def remove_dots_solution_three(string_input):
    return string_input.replace(".", "")
