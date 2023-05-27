# This module calculates and returns the length of the longest sequence of zeros in a binary string.
def find_longest_zero_sequence_solution_one(string_input):
    split_segments = string_input.split("1")
    segment_lengths = [len(segment) for segment in split_segments]
    return max(segment_lengths)


def find_longest_zero_sequence_solution_two(string_input):
    max_streak = 0
    current_streak = 0

    for character in string_input:
        if character == "0":
            current_streak += 1
        else:
            current_streak = 0
            max_streak = max(max_streak, current_streak)

    return max_streak


def find_longest_zero_sequence_solution_three(string_input):
    return max([len(segment) for segment in string_input.split("1")])
