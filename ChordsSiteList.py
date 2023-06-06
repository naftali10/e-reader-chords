from UGChordsSite import UGChordsSite
from TAB4UChordsSite import TAB4UChordsSite
from tqdm import tqdm
from multiprocessing.pool import ThreadPool
from threading import Lock

lock = Lock()
tasks_total = 0
tasks_completed = 0


def show_progress():
    global lock, tasks_total, tasks_completed
    with lock:
        tasks_completed += 1
        print(f'{tasks_completed}/{tasks_total} completed, {tasks_total-tasks_completed} remain.')


def make_chord_site(url, site_name, max_line_len):
    chord_site = None
    if site_name == 'UG':
        chord_site = UGChordsSite(url, max_line_len)
    if site_name == 'TAB4U':
        chord_site = TAB4UChordsSite(url, max_line_len)
    show_progress()
    return chord_site


class ChordsSiteList:

    _file_name = None
    _site_name = None
    _urls_file_path = None
    _chords_site_list = None
    _max_line_len = None

    def __init__(self, urls_file_path, max_line_len, site_name):
        self._file_name = urls_file_path.split('/')[-1].split('.')[0]
        self._site_name = site_name
        self._urls_file_path = urls_file_path
        self._max_line_len = max_line_len
        self.parse_urls()
        self.sort()

    def parse_urls(self):

        def load_pages_parallely():
            global tasks_total, tasks_completed
            tasks_total = len(urls)
            tasks_completed = 0
            with ThreadPool(1) as pool:
                args = [(url, self._site_name, self._max_line_len) for url in urls]
                for chord_site in pool.starmap(make_chord_site, args):
                    self._chords_site_list.append(chord_site)
            pool.close()
            pool.join()

        # Read the list of URLs from an external file
        with open(self._urls_file_path) as f:
            urls = f.readlines()
            # Remove whitespace characters like `\n` at the end of each line
            urls = [url.strip() for url in urls]

        # Iterate over the list of URLs
        self._chords_site_list = []
        load_pages_parallely()

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
    urls_file_path = 'URLs/UG-test.txt'
    chords_site_list = ChordsSiteList(urls_file_path, 150, 'UG')
    print (chords_site_list._chords_site_list[0]._song_name)
    chords_site_list.sort()
    print (chords_site_list._chords_site_list[0]._song_name)


if __name__ == '__main__':
    test()
