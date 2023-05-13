class SongLine:

    
    _text = None
    _type = None
    _width = None


    def __init__(self, text):
        self._text = text
        self._type = None
        self._width = len(text)
        

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
        return self._type is not None

    def get_type(self):
        return str(self._type)

    def is_too_long(self, width):
        return width < self._width

    def get_wrapped_text(self, page_width_in_chars):

        def split_to_words_incl_pre_whitespaces(text):

            split_list = []
            current_string = ''
            inside_a_word = False

            for char in text:
                if inside_a_word:
                    if char.isspace():
                        split_list.append(current_string)
                        current_string = char
                        inside_a_word = False
                    else:
                        current_string += char
                else:
                    current_string += char
                    if not char.isspace():
                        inside_a_word = True
            if inside_a_word:
                split_list.append(current_string)
            return split_list

        words = split_to_words_incl_pre_whitespaces(self._text)
        lines = []  # Initialize the lines list
        current_line = ""  # Initialize the current line string

        for word in words:
            if len(current_line + word) <= page_width_in_chars:
                current_line += word
            else:
                if len(word) < page_width_in_chars:
                    lines.append(current_line)
                    current_line = word
                else:
                    for i in range(0, len(word), page_width_in_chars):
                        lines.append(word[i:i + page_width_in_chars])


        lines.append(current_line)  # Add the final line to the lines list

        return "\n".join(lines)  # Join the lines with newline characters and return the result
