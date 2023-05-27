# This module takes a list as input, converts and returns the items as a string.
def convert_to_string_solution_one(list_input):
    return [item for item in list_input]


def convert_to_string_solution_two(list_input):
    return list(map(str, list_input))
