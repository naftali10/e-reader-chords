from reportlab.pdfgen import canvas
from io import BytesIO
from pdfrw import PdfWriter, PdfReader
from PIL import Image, ImageDraw, ImageFont

class MyCanvas(canvas.Canvas):

    _packet = None

    # Set custom page size in centimeters
    page_width_cm = 9
    page_height_cm = 12
    
    left_margin_cm = 0.1
    top_margin_cm = 0.3

    font = "Courier-Bold"
    font_size = 10
    Header_font = "Courier"

    # Convert page size from centimeters to points
    page_width = page_width_cm / 2.54 * 72
    page_height = page_height_cm / 2.54 * 72
    left_margin = left_margin_cm / 2.54 * 72
    top_margin = top_margin_cm / 2.54 * 72

    
    def __init__(self):
        self._packet = BytesIO()
        super().__init__(self._packet, pagesize=(self.page_width, self.page_height))

    
    def start_new_page(self, title):
        title_path = 'titles/'+title+'.png'
        self.showPage()
        image_width, image_height = self.save_title_as_image(title, title_path)
        x_for_center = (self.page_width - image_width) / 2
        y = self.page_height-image_height*1.1
        self.drawImage(title_path, x_for_center, y)
        self.setFont(self.font, self.font_size)

        
    def save_title_as_image(self, title, image_path):

        # specify the font and size
        font = ImageFont.truetype('arial.ttf', self.font_size)
        
        # Make dummy image
        image = Image.new('1', (200, 100), 'white')
        draw = ImageDraw.Draw(image)

        # calculate the size of the text
        width, height = draw.textsize(title, font)
        
        # create a new image with a white background
        image = Image.new('1', (int(width*1.1), height), 'white')
        draw = ImageDraw.Draw(image)

        # add the text to the image
        draw.text((0, 0), title, fill='black', font=font)

        # save the image
        image.save(image_path)

        return width, height


    def add_header_page(self, title):
        title_width = self.stringWidth(title, self.font, self.font_size)
        x_for_center = (self.page_width - title_width) / 2
        y = self.page_height/2
        self.showPage()
        self.setFont(self.Header_font, self.font_size)
        self.drawString(x_for_center, y, title)


    def write_to_pdf(self, pdf_path):
        self.save()
        # Move to the beginning of the StringIO buffer
        self._packet.seek(0)
        new_pdf = PdfReader(self._packet)

        # Add the new pages to PDF
        pdf_writer = PdfWriter()
        for page in new_pdf.pages:
            pdf_writer.addpage(page)
        pdf_writer.write(pdf_path)


    def write_text(self, text, title):
        
        page_num = 1
        x = self.left_margin
        y = self.page_height-self.top_margin-self._leading
                
        self.start_new_page(title+' (page 1)')
        
        lines = text.split('\n')
        for line in lines:
            self.drawString(x, y, line[:-1])
            y -= self._leading
            if y<0:
                page_num += 1
                self.start_new_page(title+f' (page {page_num})')
                y = self.page_height-self.top_margin-self._leading
    
