import ChordsSite


class UGChordsSite(ChordsSite.ChordsSite):
    
    def __init__(self, url, max_line_len):
        
        super().__init__(url)

        _language = "EN"        
        self.set_artist()
        self.set_song_name()
        self.set_song_text()

        self._web_aux.browser.quit()
        self.parse_song(max_line_len)

    def set_song_text(self):

        section = self._web_aux.soup.find("pre")
        raw_text = section.get_text()
        raw_lines = raw_text.split('\n')
        self._song_text = ''
        for line in raw_lines:
            self._song_text += line[:-1]+'\n'

    def set_artist(self):

        section = self._web_aux.soup.find('a', class_=['aPPf7 fcGj5'])

        # Extract all the song from section
        self._artist = section.get_text()

    def set_song_name(self):

        section = self._web_aux.soup.find('h1', class_=['dUjZr'])

        # Extract the title from section
        self._song_name = section.get_text()[:-7]


def test():
    url = "https://tabs.ultimate-guitar.com/tab/lady-gaga/born-this-way-chords-1028955"
    url = "https://tabs.ultimate-guitar.com/tab/britney-spears/everytime-chords-117988"
    ug_chord_site = UGChordsSite(url)
    print(ug_chord_site._song_text)
    print(ug_chord_site._artist)
    print(ug_chord_site._song_name)


# test()
