# This module takes a 2-dimensional list input and returns it flat.
def flatten_list_solution_one(list_input):
    flattened_list = []

    for sublist in list_input:
        for item in sublist:
            flattened_list.append(item)

    return flattened_list


def flatten_list_solution_two(list_input):
    return [item for inner_list in list_input for item in inner_list]
