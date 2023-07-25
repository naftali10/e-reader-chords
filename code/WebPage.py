from Song import Song
from WebAux import WebAux


class WebPage:
    _url = None
    _artist = None
    _song_name = None
    _song_text = None
    _web_aux = None
    _language = None
    _song = None
    _chord_transpose = 0
    
    def __init__(self, url, browser):
        url_breakup = url.split('|')
        if 1 < len(url_breakup):
            self._chord_transpose = int(url_breakup[-1])
        self._url = url_breakup[0]
        self._web_aux = WebAux(self._url, browser)

    def parse_song(self, max_line_len):
        self._song = Song(self._song_text, max_line_len)

    def get_title(self):
        return self._artist + ' - ' + self._song_name

    def get_song(self):
        return self._song

    def get_browser(self):
        return self._web_aux.get_browser()

    def get_soup(self):
        return self._web_aux.get_soup()
