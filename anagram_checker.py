# This module checks if two user-inputted words are anagrams and for counting the occurrences of letters in a word.
from collections import Counter


def is_anagram_solution_one(first_string_input, second_string_input):
    first_string_input_counter = Counter(first_string_input)
    second_string_input_counter = Counter(second_string_input)

    if first_string_input_counter == second_string_input_counter:
        return True
    else:
        return False


def is_anagram_solution_two(first_string_input, second_string_input):
    return sorted(first_string_input) == sorted(second_string_input)


def count_letters(any_string_input):
    return {letter: any_string_input.count(letter) for letter in any_string_input}


def is_anagram_solution_three(first_string_input, second_string_input):
    return count_letters(first_string_input) == count_letters(second_string_input)
