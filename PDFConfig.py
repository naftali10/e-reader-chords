
class PDFConfig:

    def __init__(self, page_width_cm, page_height_cm):

        self.rigid_page_height = None
        self.char_to_px = None

        self.left_margin_cm = 0.1
        self.top_margin_cm = 0.3

        self.page_width_cm = page_width_cm
        self.page_height_cm = page_height_cm

        # Use only monospace fonts
        self.font = "Courier-Bold"
        self.Header_font = "Courier"
        self.font_size = 10

        # Conversion of page size from centimeters to points
        self.cm_to_px = 72 / 2.54
        self.page_width_px = self.page_width_cm * self.cm_to_px
        self.page_height_px = self.page_height_cm * self.cm_to_px
        self.left_margin_px = self.left_margin_cm * self.cm_to_px
        self.top_margin_px = self.top_margin_cm * self.cm_to_px
