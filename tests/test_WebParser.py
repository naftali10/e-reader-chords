import unittest
import pickle
from WebParser import WebParser
from Songbook import Songbook
from WebPage import WebPage


class TestWebParser(unittest.TestCase):

    def setUp(self) -> None:
        self.webparser = WebParser()
        self.webpages = [self.obtain_webpage_asset()]
        self.songbook = Songbook()

    @staticmethod
    def obtain_webpage_asset() -> WebPage:
        pkl_file = open('assets/asset_WebPage.pkl', 'rb')
        webpage = pickle.load(pkl_file)
        pkl_file.close()
        return webpage

    def test_make_songbook(self):
        self.assertEqual(self.webparser.make_songbook([])._songs, [])
        self.assertEqual(self.webparser.make_songbook(self.webpages), [])


if __name__ == '__main__':
    unittest.main()
