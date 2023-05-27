# This module counts the number of syllables in a hyphen-separated word.
def count_syllables_solution_one(hyphenated_word_input):
    syllable_count = 0

    for letter in hyphenated_word_input:
        if letter == "-":
            syllable_count += 1

    return syllable_count + 1


def count_syllables_solution_two(hyphenated_word_input):
    return hyphenated_word_input.count("-") + 1


def count_syllables_solution_three(hyphenated_word_input):
    return len(hyphenated_word_input.split("-"))
