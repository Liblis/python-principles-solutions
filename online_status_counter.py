# This module counts the number of users who are currently online based on their status in a dictionary.
def count_online_status_solution_one(user_statuses_input):
    online_count = 0

    for user in user_statuses_input:
        if user_statuses_input[user] == "online":
            online_count += 1

    return online_count


def count_online_status_solution_two(user_statuses_input):
    return len([user for user in user_statuses_input if user_statuses_input[user] == "online"])
