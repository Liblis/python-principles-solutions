# This module checks if a given string contains any consecutive duplicate characters.
def has_consecutive_duplicates_solution_one(string_input):
    for index in range(1, len(string_input)):
        if string_input[index] == string_input[index - 1]:
            return True

    return False


def has_consecutive_duplicates_solution_two(string_input):
    for index in range(len(string_input) - 1):
        current_character = string_input[index]
        next_character = string_input[index + 1]
        if current_character == next_character:
            return True

    return False


def has_consecutive_duplicates_solution_three(string_input):
    return any([current_character == next_character for current_character, next_character in
                zip(string_input, string_input[1:])])
