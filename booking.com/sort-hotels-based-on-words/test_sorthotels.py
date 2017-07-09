import unittest

from sort_hotels import sort_hotels


class TestSortHotels(unittest.TestCase):
    def test(self):
        hotels = [
            'Do not make a reservation in this hotel even if has low low low price low price',
            'Great view and accommodation, best option for the price price price',
            'Great view and accommodation, best option for the price',
            'Best option for the price price price price'
        ]

        search_keywords = [
            'price',
            'accommodation',
            'view',
            'low',
            'best'
        ]

        self.assertTrue([1, 0, 3, 2], sort_hotels(hotels, search_keywords))
