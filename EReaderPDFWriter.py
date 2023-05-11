from PDFChordWriter import PDFChordWriter
from PDFConfig import PDFConfig


class EReaderPDFWriter (PDFChordWriter):

    _cfg = None

    def __init__(self, urls_file_path, cfg): # TODO: ditch the cfg, initiate it inside this class
        self.define_page(cfg)
        super().__init__(urls_file_path, cfg)

    def define_page(self, cfg):
        self._cfg = cfg
        self._cfg.rigid_page_height = True

    def make_pdf(self, output_file_path):

        for song in self._UG_chords_list.get_list():
            title = song.get_title()
            text = song.get_parsed_lines()
            self.write_text(text, title)

        self.finalize_pdf(output_file_path)

    def write_text(self, text, title):

        song_line_list = SongLineList(text, self.get_max_line_len())

        page_num = 1
        x = self._cfg.left_margin_px
        y = self._cfg.page_height_px - self._cfg.top_margin_px - self._leading

        self.start_new_page(title + ' (page 1)')

        lines = text.split('\n')
        for line in lines:
            self.drawString(x, y, line[:-1])
            y -= self._leading
            if y < 0:
                page_num += 1
                self.start_new_page(title + f' (page {page_num})')
                y = self._cfg.page_height_px - self._cfg.top_margin_px - self._leading

    def start_new_page(self, title):

        def print_title_as_image():

            def save_title_as_image(title, image_path):
                # specify the font and size
                font = ImageFont.truetype('arial.ttf', self._cfg.font_size)

                # Make dummy image
                image = Image.new('1', (200, 100), 'white')
                draw = ImageDraw.Draw(image)

                # calculate the size of the text
                width, height = draw.textsize(title, font)

                # create a new image with a white background
                image = Image.new('1', (int(width * 1.1), height), 'white')
                draw = ImageDraw.Draw(image)

                # add the text to the image
                draw.text((0, 0), title, fill='black', font=font)

                # save the image
                image.save(image_path)

                return width, height

            title_file_path = 'titles/' + title + '.png'
            image_width, image_height = save_title_as_image(title, title_file_path)
            x_for_center = (self._cfg.page_width_cm - image_width) / 2 # TODO: what if x<0?
            y = self._cfg.page_height_px - image_height * 1.1
            self.drawImage(title_file_path, x_for_center, y)

        self.showPage()
        print_title_as_image()
        self.setFont(self._cfg.font, self._cfg.font_size)


def test():
    from PDFConfig import PDFConfig
    cfg = PDFConfig()
    urls_file_path = 'urls.txt'
    tablet_chord_writer = EReaderPDFWriter(urls_file_path, cfg)
    pdf_file_path = 'output.pdf'
    tablet_chord_writer.make_pdf(pdf_file_path)


test()