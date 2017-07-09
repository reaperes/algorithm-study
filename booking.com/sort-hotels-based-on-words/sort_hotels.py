"""
ref: https://www.careercup.com/question?id=5689420884738048

Problem statement
Given a set of hotels and its guests reviews, sort the hotels based on a list of words specified by a user. The criteria to sort the hotels should be how many times the words specified by the user is mentioned in the hotel reviews.

Input
The first line contains a space-separated set of words which we want to find mentions in the hotel reviews.
The second line contains one integer M, which is the number of reviews.
This is followed by M+M lines, which alternates an hotel ID and a review belonging to that hotel.

Output
A list of hotel IDs sorted, in descending order, by how many mentions they have of the words specified in the input. If the count is same, sort according to the hotel IDs.
"""


def sort_hotels(hotels, search_keywords):
    hotels_point = {}

    for hotel_id in range(0, len(hotels)):
        hotel = hotels[hotel_id]
        point = 0
        for keyword in search_keywords:
            point += hotel.count(keyword)

        hotels_point[hotel_id] = point

    return [x[0] for x in sorted(hotels_point.items(), key=lambda x: (x[1], x[0]), reverse=True)]
