from TabletPDFWriter import TabletPDFWriter
import os
import sys


def produce_pdf(filepath, domain):
    print("Started processing", filepath)
    tablet_chord_writer = TabletPDFWriter(filepath, domain)
    file_name = os.path.splitext(os.path.basename(filepath))[0]
    pdf_file_path = 'output/' + file_name + '.pdf'
    tablet_chord_writer.make_pdf(pdf_file_path)
    print("Saved PDF", pdf_file_path)


def produce_pdfs(urls_dir, domain):
    for urls_file in os.listdir(urls_dir):
        filepath = os.path.join(urls_dir, urls_file)
        if not os.path.isfile(filepath):
            continue
        produce_pdf(filepath, domain)


if __name__ == '__main__':
    path = sys.argv[1]
    domain = sys.argv[2]
    if os.path.isdir(path):
        produce_pdfs(path, domain)
    elif os.path.isfile(path):
        produce_pdf(path, domain)
    print('DONE!\nExiting...')
