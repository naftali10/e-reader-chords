
class PDFConfig:

    page_width_cm = 9
    page_height_cm = 12
    rigid_page_height = None

    left_margin_cm = 0.1
    top_margin_cm = 0.3

    # Use only monospace fonts
    font = "Courier-Bold"
    Header_font = "Courier"
    font_size = 10

    # Conversion of page size from centimeters to points
    cm_to_px = 72 / 2.54
    page_width_px = page_width_cm * cm_to_px
    page_height_px = page_height_cm * cm_to_px
    left_margin_px = left_margin_cm * cm_to_px
    top_margin_px = top_margin_cm * cm_to_px
