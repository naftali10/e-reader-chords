from UGChordsSite import UGChordsSite


class ChordsSiteList:

    _urls_file_path = None
    _chords_site_list = None

    def __init__(self, urls_file_path, max_line_len):
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
            self._chords_site_list.append(UGChordsSite(url, max_line_len))
            print("Successfully appended", self._chords_site_list[-1].get_title())

    def sort(self):
        self._chords_site_list.sort(key=lambda site: (site.get_title()))

    def get_list(self):
        return self._chords_site_list

def test():
    urls_file_path = 'urls.txt'
    chords_site_list = ChordsSiteList(urls_file_path)
    print (chords_site_list._chords_site_list[0]._song_name)
    chords_site_list.sort()
    print (chords_site_list._chords_site_list[0]._song_name)
    chords_site_list.save_to_pdf("output.pdf")


# test()
