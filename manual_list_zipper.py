# This module takes two lists and zips them manually.
def zip_lists_solution_one(first_list_input, second_list_input):
    zipped_list = []

    for index in range(0, len(first_list_input)):
        zipped_list.append((first_list_input[index], second_list_input[index]))

    return zipped_list


def zip_lists_solution_two(first_list_input, second_list_input):
    zipped_list = []

    for index in range(len(first_list_input)):
        first_list_item = first_list_input[index]
        second_list_item = second_list_input[index]
        zipped_items = (first_list_item, second_list_item)
        zipped_list.append(zipped_items)

    return zipped_list


def zip_lists_solution_three(first_list_input, second_list_input):
    return [(first_list_input[index], second_list_input[index]) for index in range(len(first_list_input))]
