# This module checks if a given item is present in only one of the two provided lists.
def is_item_in_only_one_list_solution_one(item_input, first_list_input, second_list_input):
    if item_input in first_list_input and item_input not in second_list_input:
        return True
    elif item_input in second_list_input and item_input not in first_list_input:
        return True
    else:
        return False


def is_item_in_only_one_list_solution_two(item_input, first_list_input, second_list_input):
    return (item_input in first_list_input) ^ (item_input in second_list_input)


def is_item_in_only_one_list_solution_three(item_input, first_list_input, second_list_input):
    if item_input not in first_list_input and item_input not in second_list_input:
        return False
    if item_input in first_list_input and item_input in second_list_input:
        return False

    return True
