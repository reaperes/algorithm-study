import unittest
from findhotels import find_hotels


class TestFindHotel(unittest.TestCase):
    def test(self):
        users_info = [
            [2, 3, 1],
            [2, 5, 3],
            [7, 3, 1]
        ]

        print(find_hotels(users_info))

        self.assertSequenceEqual({3}, find_hotels(users_info))


if __name__ == '__main__':
    unittest.main()
