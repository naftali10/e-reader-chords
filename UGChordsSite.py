import ChordsSite

class UGChordsSite(ChordsSite.ChordsSite):
    
    def __init__(self, url):
        
        super().__init__(url)

        _language = "EN"        
        self._artist = self.get_artist_from_browser()
        self._title = self.get_title_from_browser()
        self._chords = self.get_chords_from_browser()

        self._web_aux.browser.quit()
        self.parse_chords()

    
    def get_chords_from_browser(self):

        section = self._web_aux.soup.find("pre")

        # Extract all the chords from section
        chords = section.get_text()
        
        # Rerturn the chords
        return chords


    def get_artist_from_browser(self):

        section = self._web_aux.soup.find('a', class_=['aPPf7 fcGj5'])

        # Extract all the chords from section
        artist = section.get_text()
        
        # Rerturn the chords
        return artist

    
    def get_title_from_browser(self):

        section = self._web_aux.soup.find('h1', class_=['dUjZr'])

        # Extract all the chords from section
        title = section.get_text()
        
        # Rerturn the chords
        return title[:-7]

        

def test():
    url = "https://tabs.ultimate-guitar.com/tab/lady-gaga/born-this-way-chords-1028955"
    url = "https://tabs.ultimate-guitar.com/tab/britney-spears/everytime-chords-117988"
    ug_chord_site = UGChordsSite(url)
    print (ug_chord_site._chords)
    print (ug_chord_site._artist)
    print (ug_chord_site._title)


#test()
