# This module checks if all three input values are true, and returns the resulting boolean.
def check_all_true_solution_one(first_input, second_input, third_input):
    if first_input is True and second_input is True and third_input is True:
        return True
    else:
        return False


def check_all_true_solution_two(first_input, second_input, third_input):
    return first_input and second_input and third_input
