from threading import Lock
from selenium import webdriver
from UGChordsSite import UGChordsSite
from TAB4UChordsSite import TAB4UChordsSite
from multiprocessing.pool import ThreadPool

lock = Lock()
tasks_total = 0
tasks_completed = 0
browsers = {}


class WebManager:
    _thread_num = 3

    def __init__(self, site_name, max_line_len):
        self._site_name = site_name
        self._max_line_len = max_line_len

    def load_pages_parallely(self, urls):
        global tasks_total, tasks_completed
        chords_site_list = []
        self.make_browsers()
        tasks_total = len(urls)
        tasks_completed = 0
        with ThreadPool(self._thread_num) as pool:
            args = [(url, self._site_name, self._max_line_len) for url in urls]
            for chord_site in pool.starmap(WebManager.make_chord_site, args):
                chords_site_list.append(chord_site)
        pool.close()
        pool.join()
        self.quit_browsers()
        return chords_site_list

    def make_browsers(self):
        global browsers
        browsers = {}
        options = webdriver.EdgeOptions()
        extension_dir_that_i_zipped = r"C:\Users\nafta\AppData\Local\Microsoft\Edge\User Data\\" + \
                                      r"Profile 1\Extensions\uBlock.zip"
        options.add_extension(extension_dir_that_i_zipped)
        for i in range(self._thread_num):
            browsers[webdriver.Edge(options=options)] = 'free'

    @staticmethod
    def quit_browsers():
        global browsers
        for browser in browsers:
            browser.quit()

    @staticmethod
    def make_chord_site(url, site_name, max_line_len):
        chord_site = None
        browser = WebManager.acquire_browser()
        browser.implicitly_wait(3)
        if site_name == 'UG':
            chord_site = UGChordsSite(url, max_line_len, browser)
        if site_name == 'TAB4U':
            chord_site = TAB4UChordsSite(url, max_line_len, browser)
        WebManager.release_browser(browser)
        WebManager.show_progress()
        return chord_site

    @staticmethod
    def acquire_browser():
        global lock
        with lock:
            for browser in browsers:
                if browsers[browser] == 'free':
                    browsers[browser] = 'taken'
                    return browser

    @staticmethod
    def release_browser(browser):
        global lock
        with lock:
            browsers[browser] = 'free'

    @staticmethod
    def show_progress():
        global lock, tasks_total, tasks_completed
        with lock:
            tasks_completed += 1
            print(f'{tasks_completed}/{tasks_total} completed, {tasks_total - tasks_completed} remain.')
