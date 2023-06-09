from PDFChordWriter import PDFChordWriter
from PDFConfig import PDFConfig
import re


class TabletPDFWriter (PDFChordWriter):

    _cfg = None

    def __init__(self, urls_file_path, site_name):
        self.configure_page()
        super().__init__(urls_file_path, site_name)

    def configure_page(self):

        page_width_cm = 13.5
        page_height_cm = 22

        self._cfg = PDFConfig(page_width_cm, page_height_cm)
        self._cfg.rigid_page_height = False

    def make_pdf(self, output_file_path):

        for song in self._chord_site_list.get_list():
            title = song.get_title()
            parsed_line_list = song.get_parsed_lines()
            self.write_text(parsed_line_list, title)

        self.finalize_pdf(output_file_path)

    def write_text(self, parsed_line_list, title):

        self.start_new_page(parsed_line_list.get_len(), title)

        x = self._cfg.left_margin_px
        y = self._cfg.page_height_px - self._cfg.top_margin_px - self._leading * 2

        for parsed_line in parsed_line_list.get_list():
            if self._chord_site_list.get_language() == 'EN':
                self.drawString(x, y, parsed_line.get_text())
            if self._chord_site_list.get_language() == 'HE':
                if parsed_line.get_language() == 'EN':
                    self.drawRightString(self._cfg.page_width_px-x, y, parsed_line.get_text())
                if parsed_line.get_language() == 'HE':
                    self.drawRightString(self._cfg.page_width_px-x, y, parsed_line.get_text()[::-1])
            y -= self._leading

    def start_new_page(self, num_of_rows, title):

        def print_title_as_text():
            x_for_center = max(0, (self._cfg.page_width_px - len(title)*self._cfg.char_to_px) / 2)
            y = self._cfg.page_height_px - self._leading * 1.1
            if re.search(r'[א-ת]', title):
                self.drawString(x_for_center, y, title[::-1])
            else:
                self.drawString(x_for_center, y, title)

        self.showPage()
        self._cfg.page_height_px = (num_of_rows + 2) * self._cfg.font_size * 1.2 + self._cfg.top_margin_px
        self.setPageSize((self._cfg.page_width_px, self._cfg.page_height_px))
        self.setFont(self._cfg.font, self._cfg.font_size)
        print_title_as_text()


def test():
    UG_urls_file_path = '../input_url_lists/TAB4U-test.txt'
    tablet_chord_writer = TabletPDFWriter(UG_urls_file_path, 'TAB4U')
    pdf_file_path = 'output_pdfs/'+UG_urls_file_path.split('/')[-1].split('.')[0]+'.pdf'
    tablet_chord_writer.make_pdf(pdf_file_path)


# test()
