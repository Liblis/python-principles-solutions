# This module finds and returns the indices of all capital letters in a given string.
from string import ascii_uppercase


def find_uppercase_indices_solution_one(string_input):
    uppercase_indices = []

    for index in range(len(string_input)):
        if string_input[index].isupper():
            uppercase_indices.append(index)

    return uppercase_indices


def find_uppercase_indices_solution_two(string_input):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    indices_list = []

    for index, letter in enumerate(string_input):
        if letter in uppercase_letters:
            indices_list.append(index)

    return indices_list


def find_uppercase_indices_solution_three(string_input):
    return [index for index in range(len(string_input)) if string_input[index] in ascii_uppercase]
