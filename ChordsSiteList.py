from UGChordsSite import UGChordsSite
from TAB4UChordsSite import TAB4UChordsSite


class ChordsSiteList:

    _site_name = None
    _urls_file_path = None
    _chords_site_list = None

    def __init__(self, urls_file_path, max_line_len, site_name):
        self._site_name = site_name
        self._urls_file_path = urls_file_path
        self.parse_urls(max_line_len)
        self.sort()

    def parse_urls(self, max_line_len):
        # Read the list of URLs from an external file
        with open(self._urls_file_path) as f:
            urls = f.readlines()
            
            # Remove whitespace characters like `\n` at the end of each line
            urls = [url.strip() for url in urls]

        # Iterate over the list of URLs
        self._chords_site_list = []
        for url in urls:
            if self._site_name == 'UG':
                self._chords_site_list.append(UGChordsSite(url, max_line_len))
            if self._site_name == 'TAB4U':
                self._chords_site_list.append(TAB4UChordsSite(url, max_line_len))
            print("Successfully appended", self._chords_site_list[-1].get_title())

    def sort(self):
        self._chords_site_list.sort(key=lambda site: (site.get_title()))

    def get_list(self):
        return self._chords_site_list

    def get_language(self):
        if self._site_name == 'UG':
            return 'EN'
        if self._site_name == 'TAB4U':
            return 'HE'

    def get_setlist(self):
        setlist = []
        for chords_site in self._chords_site_list:
            setlist.append(chords_site.get_title())
        return setlist

def test():
    urls_file_path = 'URLs/UG-URLs.txt'
    chords_site_list = ChordsSiteList(urls_file_path)
    print (chords_site_list._chords_site_list[0]._song_name)
    chords_site_list.sort()
    print (chords_site_list._chords_site_list[0]._song_name)
    chords_site_list.save_to_pdf("output.pdf")


# test()
