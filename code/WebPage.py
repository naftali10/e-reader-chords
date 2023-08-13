from Song import Song
from WebAux import WebAux


class WebPage:

    _url: str
    _artist: str
    _song_name: str
    _song_text: str
    _web_aux: WebAux
    _language: str
    _song: Song
    _chord_transpose: int = 0
    
    def __init__(self, url, browser):
        url_breakup = url.split('|')
        if 1 < len(url_breakup):
            self._chord_transpose = int(url_breakup[-1])
        self._url = url_breakup[0]
        self._web_aux = WebAux(self._url, browser)

    def __eq__(self, other: 'WebPage'):
        return (
                self._url == other._url and
                self._artist == other._artist and
                self._song_name == other._song_name and
                self._language == other._language and
                self._chord_transpose == other._chord_transpose
        )

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
