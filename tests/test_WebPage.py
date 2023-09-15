import unittest
from WebPage import WebPage
from selenium import webdriver
from bs4 import BeautifulSoup


class TestWebPage(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://tabs.ultimate-guitar.com/tab/major-lazer/lean-on-chords-1734407'
        self.w = WebPage(self.url)
        self.ref = WebPage(self.url)

    def test_eq(self) -> None:
        self.assertEqual(self.w, self.ref)

    # def test_store_content(self) -> None:
    #     options = webdriver.EdgeOptions()
    #     browser = webdriver.Edge(options=options)
    #     browser.get(self.url)
    #     soup = BeautifulSoup(browser.page_source, "html.parser")
    #     self.w.store_content(browser)
    #     self.assertEqual(self.w._content, soup)


if __name__ == '__main__':
    unittest.main()
