from selenium import webdriver
from bs4 import BeautifulSoup
from SongLineList import SongLineList


class ChordsSite:
    _url = None
    _artist = None
    _song_name = None
    _song_text = None
    _web_aux = None
    _language = None
    _parsed_lines = None
    
    class WebAux:
        browser = None
        soup = None
        
        def __init__(self, url):
            # Launch a headless Edge browser using Selenium
            options = webdriver.EdgeOptions()
            options.use_chromium = True
            options.add_argument('headless')
            self.browser = webdriver.Edge(options=options)
            
            self.browser.get(url)

            # Wait for the page to fully render
            self.browser.implicitly_wait(3)

            # Use BeautifulSoup to parse the HTML content of the website
            self.soup = BeautifulSoup(self.browser.page_source, "html.parser")
    
    def __init__(self, url):
        self._url = url
        self._web_aux = ChordsSite.WebAux(url)

    def parse_song(self, max_line_len):
        self._parsed_lines = SongLineList(self._song_text, max_line_len)

    def get_title(self):
        return self._artist + ' - ' + self._song_name

    def get_parsed_lines(self):
        return self._parsed_lines
