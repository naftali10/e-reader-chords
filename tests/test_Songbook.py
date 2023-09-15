import unittest
from Songbook import Songbook


class TestSongbook(unittest.TestCase):

    def test_init(self):
        self.assertEqual(Songbook()._songs, [])


if __name__ == '__main__':
    unittest.main()
