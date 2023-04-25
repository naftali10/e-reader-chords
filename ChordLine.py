class ChordLine:

    
    _text = None
    _type = None


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
        return self._type
