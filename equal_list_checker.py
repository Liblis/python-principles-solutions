# This module takes a list input and check if all the items in the list are the same.
def check_items_solution_one(list_input):
    for index in range(1, len(list_input)):
        if not list_input[index] == list_input[index - 1]:
            return False

    return True


def check_items_solution_two(list_input):
    for item_one in list_input:
        for item_two in list_input:
            if item_one != item_two:
                return False

    return True


def check_items_solution_three(list_input):
    return all(item_one == item_two for item_one in list_input for item_two in list_input)
