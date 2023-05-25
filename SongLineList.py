import re
from SongLine import SongLine


class SongLineList:

    _song_line_list = None
    _page_width_in_chars = None

    def __init__(self, lines, page_width_in_chars):
        self._page_width_in_chars = page_width_in_chars
        self.init_list(lines, page_width_in_chars)
        self.parse_empty()
        self.parse_headings()
        self.parse_lyrics()
        self.parse_chords()
        self.wrap_lines()

    def get_len(self):
        return len(self._song_line_list)

    def get_list(self):
        return self._song_line_list

    def init_list(self, lines, page_width_in_chars):
        self._song_line_list = []
        lines = lines.split('\n')
        for line in lines:
            self._song_line_list.append(SongLine(line[:-1], page_width_in_chars))

    def parse_empty(self):
        empty_pattern = r"^\s*$"
        for song_line in self._song_line_list:
            if re.match(empty_pattern, song_line.get_text()):
                song_line.set_type_empty()

    def parse_headings(self):
        heading_pattern = r"^\W*\[.*\]\W*$"
        for song_line in self._song_line_list:
            if re.match(heading_pattern, song_line.get_text()):
                song_line.set_type_heading()

    def parse_lyrics(self):
        word_pattern = r"([a-zA-Z\'\,\.\"\(\)\-\:]{2,}|I)"
        lyrics_pattern = r"\W*"+word_pattern+r"\W+"+word_pattern+r"\W+"+word_pattern+r"\W*"
        for song_line in self._song_line_list:
            if re.match(lyrics_pattern, song_line.get_text()):
                song_line.set_type_lyrics()

    def parse_chords(self):
        chord_pattern = r"^[abdgijmsuA-G245679+#/ ]+$"
        for i in range(len(self._song_line_list) - 1):
            if re.match(chord_pattern, self._song_line_list[i].get_text()):
                if self._song_line_list[i + 1].is_lyrics():
                    self._song_line_list[i].set_type_chords()

    def wrap_lines(self):

        # Cases:
        # Long line, no type - no wrapping
        # Long lyrics with short chords or no chords - wrap only lyrics
        # Long lyrics with long chords - wrap them together
        # Long chords with no lyrics - wrap only chords
        # Long chords with short lyrics - wrap them together

        new_line_list = []
        skip_line = False

        for line_idx, song_line in enumerate(self._song_line_list):

            if skip_line:
                skip_line = False
                continue

            if 0 < line_idx:
                prev_line = self._song_line_list[line_idx-1]
            else:
                prev_line = None
            if line_idx+1 < len(self._song_line_list):
                next_line = self._song_line_list[line_idx+1]
            else:
                next_line = None

            line_replacement = [song_line]

            if song_line.is_chords() and song_line.is_too_long():
                if next_line is not None:
                    if next_line.is_lyrics():
                        if next_line.is_too_long():
                            continue
                        else:
                            line_replacement = song_line.wrap_within_reference([next_line])
                            skip_line = True
                    else:
                        line_replacement = song_line.split_to_wrapped_lines()
                else:
                    line_replacement = song_line.split_to_wrapped_lines()

            if song_line.is_lyrics() and song_line.is_too_long():
                if prev_line is not None:
                    if prev_line.is_chords():
                        if prev_line.is_too_long():
                            line_replacement = prev_line.wrap_within_reference(song_line.split_to_wrapped_lines())
                        else:
                            line_replacement = song_line.split_to_wrapped_lines()
                    else:
                        line_replacement = song_line.split_to_wrapped_lines()
                else:
                    line_replacement = song_line.split_to_wrapped_lines()

            new_line_list += line_replacement

        self._song_line_list = new_line_list


def test():
    text = ("\nIt doesn't matter if you love him, or capital H-I-M \n" +
            "Bm\nJust put your paws up \n" +
            "Bm\n'Cause you were Born This Way, baby \n \n" +
            "E5    D5     A5    E5 \n \n \n[Verse] \n \n" +
            "E                     D \n" +
            "My mama told me when I was young \n" +
            "A          Asus           Amaj7     Bm \n" +
            "We are all born superstars \n" +
            "E                              D \n" +
            "She rolled my hair and put my lipstick on \n" +
            "A               Asus2           Amaj7     Bm7 \n" +
            "In the glass of her boudoir \n \n" +
            "E                                   D \n" +
            "There's nothin' wrong with lovin' who you are \n" +
            "A                              A5 \n" +
            "She said, Cause he made you perfect, babe \n" +
            "E                                       D \n" +
            "So hold your head up, girl and you you'll go far,\n" +
            "A                    A5 \n" +
            "listen to me when I say \n \n \n[Pre-Chorus]"
            )
    text = ("                    Am         G           F       G      Esus4                 E     F \n" +
            "All the leaves are brown                  and the sky is gray \n" +
            "( All the leaves are brown )             (and the skies are grey ey )")
    song_line_list = SongLineList(text, 50)
    for song_line in song_line_list._song_line_list:
        print(song_line.get_text()+"| "+song_line.get_type())


# test()
