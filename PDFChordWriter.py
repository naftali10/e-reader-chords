from reportlab.pdfgen import canvas
from io import BytesIO
from pdfrw import PdfWriter, PdfReader

from ChordsSiteList import *


class PDFChordWriter(canvas.Canvas):

    _packet = None
    _cfg = None
    _chord_site_list = None

    def __init__(self, urls_file_path, site_name):
        self._packet = BytesIO()
        super().__init__(self._packet, pagesize=(self._cfg.page_width_cm, self._cfg.page_height_px))
        self._cfg.char_to_px = self.stringWidth('A', self._cfg.font, self._cfg.font_size)
        self._chord_site_list = ChordsSiteList(urls_file_path, self.get_max_line_len(), site_name)

    def add_header_page(self, title):
        title_width = self.stringWidth(title, self._cfg.font, self._cfg.font_size)
        x_for_center = (self._cfg.page_width_cm - title_width) / 2
        y = self._cfg.page_height_px / 2
        self.showPage()
        self.setFont(self._cfg.header_font, self._cfg.font_size)
        self.drawString(x_for_center, y, title)

    def finalize_pdf(self, pdf_path):
        self.save()
        # Move to the beginning of the StringIO buffer
        self._packet.seek(0)
        new_pdf = PdfReader(self._packet)

        # Add the new pages to PDF
        pdf_writer = PdfWriter()
        for page in new_pdf.pages:
            pdf_writer.addpage(page)
        pdf_writer.write(pdf_path)

    def get_max_line_len(self):
        return int(self._cfg.page_width_px / self._cfg.char_to_px)


def test():
    from PDFConfig import PDFConfig
    cfg = PDFConfig()
    urls_file_path = 'URLs/UG-URLs.txt'
    pdf_chord_writer = PDFChordWriter(urls_file_path, cfg)
    pdf_file_path = 'output.pdf'
    pdf_chord_writer.finalize_pdf(pdf_file_path)


# test()
