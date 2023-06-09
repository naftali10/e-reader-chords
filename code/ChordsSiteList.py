from WebManager import WebManager


class ChordsSiteList:

    _file_name = None
    _site_name = None
    _urls_file_path = None
    _chords_site_list = []
    _max_line_len = None

    def __init__(self, urls_file_path, max_line_len, site_name):
        self._web_manager = WebManager(site_name, max_line_len)
        self._file_name = urls_file_path.split('/')[-1].split('.')[0]
        self._site_name = site_name
        self._urls_file_path = urls_file_path
        self._max_line_len = max_line_len
        self.parse_urls()
        self.sort()

    def parse_urls(self):
        with open(self._urls_file_path) as f:
            urls = f.readlines()
            # Remove whitespace characters like `\n` at the end of each line
            urls = [url.strip() for url in urls]
        self._chords_site_list = []
        self._chords_site_list = self._web_manager.load_pages_parallely(urls)

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

    def get_file_name(self):
        return self._file_name


def test():
    urls_file_path = '../input_url_lists/UG-test.txt'
    chords_site_list = ChordsSiteList(urls_file_path, 150, 'UG')
    print (chords_site_list._chords_site_list[0]._song_name)
    chords_site_list.sort()
    print (chords_site_list._chords_site_list[0]._song_name)


if __name__ == '__main__':
    test()
