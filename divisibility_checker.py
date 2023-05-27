# This module checks whether a given number is divisible by three.
def is_divisible_by_three_solution_one(number_input):
    if number_input % 3 == 0:
        return True
    else:
        return False


def is_divisible_by_three_solution_two(number_input):
    return number_input % 3 == 0
