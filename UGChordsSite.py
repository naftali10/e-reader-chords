import ChordsSite
from selenium.webdriver.common.by import By


class UGChordsSite(ChordsSite.ChordsSite):

    def __init__(self, url, max_line_len, browser):
        
        super().__init__(url, browser)

        self._language = "EN"
        self.set_artist()
        self.set_song_name()
        self.transpose_chords()
        self.set_song_text()

        self.parse_song(max_line_len)

    def set_song_text(self):

        section = self.get_soup().find("pre")
        raw_text = section.get_text()
        raw_lines = raw_text.split('\n')
        self._song_text = ''
        for line in raw_lines:
            self._song_text += line[:-1]+'\n'

    def set_artist(self):

        section = self.get_soup().find('a', class_=['aPPf7 fcGj5'])

        # Extract all the song from section
        self._artist = section.get_text()

    def set_song_name(self):

        section = self.get_soup().find('h1', class_=['dUjZr'])

        # Extract the title from section
        self._song_name = section.get_text()[:-7]

    def transpose_chords(self):
        down_button = self.get_browser().find_elements(
            By.CLASS_NAME,
            value='ovH1k.rPQkl.mcpNL.IxFbd.gm3Af.lTEpj.mLpXg')[2]
        up_button = self.get_browser().find_elements(
            By.CLASS_NAME,
            value='ovH1k.rPQkl.mcpNL.IxFbd.gm3Af.lTEpj.mLpXg')[3]
        if self._chord_transpose < 0:
            for i in range(abs(self._chord_transpose)):
                down_button.click()
        if 0 < self._chord_transpose:
            for i in range(abs(self._chord_transpose)):
                up_button.click()
        self._web_aux.reload()


def test():
    url = "https://tabs.ultimate-guitar.com/tab/lady-gaga/born-this-way-chords-1028955"
    url = "https://tabs.ultimate-guitar.com/tab/britney-spears/everytime-chords-117988|+1"
    ug_chord_site = UGChordsSite(url, 50)
    print(ug_chord_site._song_text)
    print(ug_chord_site._artist)
    print(ug_chord_site._song_name)


# test()
