import re
from ChordLine import ChordLine

class ChordLineList:
    _chord_line_list = None
    
    def __init__(self, chords):
        self.init_list(chords)
        self.parse_empty()
        self.parse_headings()
        self.parse_lyrics()
        self.parse_chords()


    def init_list(self, chords):
        self._chord_line_list = []
        lines = chords.split('\n')
        for line in lines:
            self._chord_line_list.append(ChordLine(line))


    def parse_empty(self):
        empty_pattern = r"^\s*$"
        for chord_line in self._chord_line_list:
            if re.match(empty_pattern, chord_line.get_text()):
                chord_line.set_type_empty()


    def parse_headings(self):
        heading_pattern = r"^\W*\[.*\]\W*$"
        for chord_line in self._chord_line_list:
            if re.match(heading_pattern, chord_line.get_text()):
                chord_line.set_type_heading()


    def parse_lyrics(self):
        word_pattern = r"([a-zA-Z',.]{2,}|I)"
        lyrics_pattern = word_pattern+r"\W"+word_pattern+r"\W"+word_pattern
        for chord_line in self._chord_line_list:
            if re.match(lyrics_pattern, chord_line.get_text()):
                chord_line.set_type_lyrics()


    def parse_chords(self):
        chord_pattern = r"^[a-zA-Z245679+#/ ]+$"
        for i in range(len(self._chord_line_list)-1):
            if re.match(chord_pattern, self._chord_line_list[i].get_text()):
                if self._chord_line_list[i+1].is_lyrics():
                    self._chord_line_list[i].set_type_chords()


    def wrap_line (self, line_number):
        return
    

def test():
    text = ("\nIt doesn't matter if you love him, or capital H-I-M \n"+
            "Bm\nJust put your paws up \n"+
            "Bm\n'Cause you were Born This Way, baby\n \n"+
            "E5    D5     A5    E5\n \n \n[Verse]\n \n"+
            "E                     D\n"+
            "My mama told me when I was young \n"+
            "A          Asus           Amaj7     Bm\n"+
            "We are all born superstars \n+"+
            "E                              D\n"+
            "She rolled my hair and put my lipstick on \n"+
            "A               Asus2           Amaj7     Bm7\n"+
            "In the glass of her boudoir \n \n"+
            "E                                   D\n"+
            "There's nothin' wrong with lovin' who you are \n"+
            "A                              A5\n"+
            "She said, Cause he made you perfect, babe \n"+
            "E                                       D\n"+
            "So hold your head up, girl and you you'll go far,\n"+
            "A                    A5\n"+
            "listen to me when I say \n \n \n[Pre-Chorus]"
            )
    chord_line_list = ChordLineList(text)
    print(chord_line_list._chord_line_list[0].get_text())
    print(chord_line_list._chord_line_list[2].is_heading())
    for chord_line in chord_line_list._chord_line_list:
        print(chord_line.get_text()+"   -   "+chord_line.get_type())

#test()
