# This module extracts, validates and returns the middle indices of a list.
def find_middle_solution_one(string_input):
    if len(string_input) % 2 == 0:
        return "There is no middle."
    else:
        index = round(len(string_input) / 2)
        return string_input[index - 1]


def find_middle_solution_two(string_input):
    if len(string_input) % 2 == 0:
        return "There is no middle."
    else:
        return string_input[len(string_input) // 2]
