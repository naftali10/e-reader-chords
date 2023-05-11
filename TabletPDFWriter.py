from PDFChordWriter import PDFChordWriter
from PDFConfig import PDFConfig


class TabletPDFWriter (PDFChordWriter):

    _cfg = None

    def __init__(self, urls_file_path, cfg): # TODO: ditch the input cfg, initiate it inside this class
        self.define_page(cfg)
        super().__init__(urls_file_path, cfg)

    def define_page(self, cfg):
        self._cfg = cfg
        self._cfg.rigid_page_height = False

    def make_pdf(self, output_file_path):

        for song in self._UG_chords_list.get_list():
            title = song.get_title()
            parsed_line_list = song.get_parsed_lines()
            self.write_text(parsed_line_list, title)

        self.finalize_pdf(output_file_path)

    def write_text(self, parsed_line_list, title):

        self.start_new_page(parsed_line_list.get_len(), title)

        x = self._cfg.left_margin_px
        y = self._cfg.page_height_px - self._cfg.top_margin_px - self._leading

        for parsed_line in parsed_line_list.get_list():
            self.drawString(x, y, parsed_line.get_text())
            y -= self._leading

    def start_new_page(self, num_of_rows, title):

        def print_title_as_text():
            x_for_center = (self.get_max_line_len() - len(title)) / 2  # TODO: what if x<0?
            y = self._cfg.page_height_px - self._leading * 1.1
            self.drawString(x_for_center, y, title)

        self.showPage()
        self._cfg.page_height_px = (num_of_rows + 2) * self._cfg.font_size * 1.2 + self._cfg.top_margin_px
        self.setPageSize((self._cfg.page_width_px, self._cfg.page_height_px))
        self.setFont(self._cfg.font, self._cfg.font_size)
        print_title_as_text()


def test():
    from PDFConfig import PDFConfig
    cfg = PDFConfig()
    urls_file_path = 'urls.txt'
    tablet_chord_writer = TabletPDFWriter(urls_file_path, cfg)
    pdf_file_path = 'output.pdf'
    tablet_chord_writer.make_pdf(pdf_file_path)


test()
