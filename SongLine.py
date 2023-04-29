class SongLine:

    
    _text = None
    _type = None
    _width = None


    def __init__(self, text):
        self._text = text
        self._type = None
        

    def get_text(self):
        return self._text

    def set_type_empty(self):
        self._type = 'MT'


    def set_type_lyrics(self):
        self._type = 'LY'


    def set_type_chords(self):
        self._type = 'CH'


    def set_type_heading(self):
        self._type = 'HD'


    def is_empty(self):
        return self._type == 'MT'


    def is_lyrics(self):
        return self._type == 'LY'


    def is_chords(self):
        return self._type == 'CH'


    def is_heading(self):
        return self._type == 'HD'


    def is_type_set(self):
        return self._type != None


    def get_type(self):
        return str(self._type)


    def set_width(self, width):
        self._width = width


    def get_width(self):
        return self._width


    def get_wrapped_text(self, page_width):

        words = self._text.split()  # Split the text into words
        lines = []  # Initialize the lines list
        current_line = ""  # Initialize the current line string

        for word in words:
            if len(current_line + word) + 1 <= page_width:
                current_line += word + " "  # Add the word to the current line
            else:
                lines.append(current_line.strip())  # Add the current line to the lines list
                current_line = word + " "  # Start a new line with the current word

        lines.append(current_line.strip())  # Add the final line to the lines list

        return "\n".join(lines)  # Join the lines with newline characters and return the result
