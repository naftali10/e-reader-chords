import ChordsSite

class UGChordsSite(ChordsSite.ChordsSite):
    
    def __init__(self, url):
        
        super().__init__(url)

        _language = "EN"        
        self._artist = self.get_artist_from_browser()
        self._title = self.get_title_from_browser()
        self._song = self.get_song_from_browser()

        self._web_aux.browser.quit()
        self.parse_song()

    
    def get_song_from_browser(self):

        section = self._web_aux.soup.find("pre")

        # Extract all the song from section
        song = section.get_text()
        
        # Rerturn the song
        return song


    def get_artist_from_browser(self):

        section = self._web_aux.soup.find('a', class_=['aPPf7 fcGj5'])

        # Extract all the song from section
        artist = section.get_text()
        
        # Rerturn the song
        return artist

    
    def get_title_from_browser(self):

        section = self._web_aux.soup.find('h1', class_=['dUjZr'])

        # Extract the titile from section
        title = section.get_text()
        
        # Rerturn the title
        return title[:-7]

        

def test():
    url = "https://tabs.ultimate-guitar.com/tab/lady-gaga/born-this-way-chords-1028955"
    url = "https://tabs.ultimate-guitar.com/tab/britney-spears/everytime-chords-117988"
    ug_chord_site = UGChordsSite(url)
    print (ug_chord_site._song)
    print (ug_chord_site._artist)
    print (ug_chord_site._title)


#test()
