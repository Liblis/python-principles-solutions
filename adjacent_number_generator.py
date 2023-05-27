# This module returns a tuple of the numbers immediately before and after a given input number.
def generate_adjacent_numbers_solution_one(number_input):
    adjacent_numbers = (number_input - 1, number_input + 1)
    return adjacent_numbers


def generate_adjacent_numbers_solution_two(number_input):
    return number_input - 1, number_input + 1
