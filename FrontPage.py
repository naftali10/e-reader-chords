from reportlab.pdfgen import canvas
from io import BytesIO
from pdfrw import PdfReader


class FrontPage (canvas.Canvas):

    _packet = None
    _cfg = None
    _setlist = None
    _pdf = None

    def __init__(self, chord_site_list, cfg):
        self._packet = BytesIO()
        self._cfg = cfg
        super().__init__(self._packet, pagesize=(self._cfg.page_width_cm, self._cfg.page_height_px))
        self._setlist = chord_site_list.get_setlist()
        self.generate_page()

    def generate_page(self):
        num_of_rows = len(self._setlist)
        self._cfg.page_height_px = (num_of_rows + 2) * self._cfg.font_size * 1.2 + self._cfg.top_margin_px
        self.setPageSize((self._cfg.page_width_px, self._cfg.page_height_px))
        self.setFont(self._cfg.font, self._cfg.font_size)

        x = self._cfg.left_margin_px
        y = self._cfg.page_height_px - self._cfg.top_margin_px - self._leading * 2
        for title in self._setlist:
            self.drawString(x, y, title)
            y -= self._leading

        self.save()
        self._packet.seek(0)
        self._pdf = PdfReader(self._packet)

    def get_page(self):
        return self._pdf.pages[0]

