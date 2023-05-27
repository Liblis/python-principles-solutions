# This module converts a user's letter-number choice into corresponding row and column indices in a matrix.
def get_row_column_solution_one(user_choice_input):
    letter_to_index = {"A": 0, "B": 1, "C": 2}
    letter = user_choice_input[0]
    number = user_choice_input[1]
    row = int(number) - 1
    column = letter_to_index[letter]
    return row, column


def get_row_column_solution_two(user_choice_input):
    letter_to_index = {"A": 0, "B": 1, "C": 2}
    number_to_index = {"1": 0, "2": 1, "3": 2}
    return number_to_index[user_choice_input[1]], letter_to_index[user_choice_input[0]]
