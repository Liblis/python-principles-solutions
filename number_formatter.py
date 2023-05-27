# This module formats a number by inserting commas every three digits.
def format_number_solution_one(number_input):
    reversed_digits = [digit for digit in str(number_input)[::-1]]
    new_reversed_digits = []

    for index, digit in enumerate(reversed_digits):
        new_reversed_digits.append(digit)
        if (index + 1) % 3 == 0 and (index + 1) != len(reversed_digits):
            new_reversed_digits.append(",")

    return ''.join(new_reversed_digits[::-1]).lstrip(',')


def format_number_solution_two(number_input):
    result = ""

    for index, digit in enumerate(reversed(str(number_input))):
        if index != 0 and (index % 3) == 0:
            result += ","
        result += digit

    return result[::-1]


def format_number_solution_three(number_input):
    return "{:,}".format(number_input)
