from ebooklib import epub

# create a new EPUB book
#book = epub.EpubBook()
book = epub.read_epub('my_epub_book.epub')

# set the metadata
book.set_title('Naftali\'s Chords (EN)')
book.set_language('en')

# create a new chapter
chapter = epub.EpubHtml(title='Chapter 2', file_name='chapter2.xhtml', lang='en')

# set the content of the chapter
#chapter.content = (
#    "<h1>Chapter 2</h1  >"
#    "<p>This is some text that will be saved to EPUB.</p>"
#)

# add the chapter to the book
#book.add_item(chapter)

# create the table of contents
#book.toc = [epub.Link('chapter2.xhtml', 'Chapter 2', 'chapter2')]

# add the table of contents to the book
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# create the spine
#book.spine = [chapter]

# create the EPUB file
epub.write_epub('Naftali\'s Chords.epub', book, {})

