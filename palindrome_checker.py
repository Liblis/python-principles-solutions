# This module checks whether a given string is a palindrome.
def is_palindrome_solution_one(string_input):
    if string_input == string_input[::-1]:
        return True
    else:
        return False


def is_palindrome_solution_two(string_input):
    while len(string_input) > 1:
        head = string_input[0]
        tail = string_input[-1]
        string_input = string_input[1:-1]
        if head != tail:
            return False

    return True


def is_palindrome_solution_three(string_input):
    if len(string_input) < 2:
        return True

    return string_input[0] == string_input[-1] and is_palindrome_solution_three(string_input[1:-1])


def is_palindrome_solution_four(string_input):
    return string_input == string_input[::-1]
