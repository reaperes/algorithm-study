"""
booking.con interview question (https://www.careercup.com/question?id=5664081785651200)

Given arrays for N (>= 2) users, each representing the IDs of hotels
visited, find the common IDs of the hotels visited amongst the users.

Input:
userA = {2, 3, 1}
userB = {2, 5, 3}
userC = {7, 3, 1}

Output:
{3}

Assumptions:
Arrays are unsorted.

Cases:
1) Each array consists of distinct hotel IDs
2) Each array may6 contain duplicate hotel IDs
"""


def find_hotels(users_info):
    hotels = set(users_info[0])
    for i in range(1, len(users_info)):
        hotels = hotels.intersection(users_info[i])
    return hotels
