# This module returns the difference between the maximum and minimum values in a given list of numbers.
def subtract_min_max_solution_one(numbers_list_input):
    return max(numbers_list_input) - min(numbers_list_input)


def subtract_min_max_solution_two(numbers_list_input):
    smallest = min(numbers_list_input)
    largest = max(numbers_list_input)
    return largest - smallest
