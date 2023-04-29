from UGChordsSite import UGChordsSite
from MyCanvas import MyCanvas

class ChordsSiteList:
    _urls_file_path = None
    _chords_site_list = None


    def __init__(self, urls_file_path):
        self._urls_file_path = urls_file_path
        self.parse_urls()


    def parse_urls(self):
        # Read the list of URLs from an external file
        with open(self._urls_file_path) as f:
            urls = f.readlines()
            
        # Remove whitespace characters like `\n` at the end of each line
            urls = [url.strip() for url in urls]

        # Iterate over the list of URLs
        self._chords_site_list = []
        for url in urls:
            self._chords_site_list.append(UGChordsSite(url))


    def sort(self):
        
        self._chords_site_list.sort(key=lambda site: (site._artist + site._title))


    def save_to_pdf(self, pdf_path):
        
        can = MyCanvas()

        for chords_site in self._chords_site_list:
            title = chords_site._artist + ' - ' + chords_site._title
            text = chords_site._song
            can.add_header_page(title)
            can.write_text(text, title)
                    
        can.write_to_pdf(pdf_path)
        

def test():
    urls_file_path = 'urls.txt'
    chords_site_list = ChordsSiteList(urls_file_path)
    print (chords_site_list._chords_site_list[0]._title)
    chords_site_list.sort()
    print (chords_site_list._chords_site_list[0]._title)
    chords_site_list.save_to_pdf("output.pdf")

test()
