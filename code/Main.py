from PDFWriterForTablet import PDFWriterForTablet
import os
import sys


def produce_pdf(filepath, domain):
    print("Started processing", filepath)
    pdf_writer = PDFWriterForTablet(filepath, domain)
    file_name = os.path.splitext(os.path.basename(filepath))[0]
    pdf_file_path = '../output_pdfs/' + file_name + '.pdf'
    pdf_writer.make_pdf(pdf_file_path)
    print("Saved PDF", pdf_file_path)


def produce_pdfs(urls_dir, domain_name):
    for urls_file in os.listdir(urls_dir):
        filepath = os.path.join(urls_dir, urls_file)
        if not os.path.isfile(filepath):
            continue
        produce_pdf(filepath, domain_name)


def check_path(urls_path):
    if not os.path.exists(urls_path):
        raise ValueError(f"Path specified ({urls_path}) does not exist")


def check_domain(urls_domain):
    if urls_domain != 'UG' and urls_domain != 'TAB4U':
        raise ValueError(f"Domain specified ({urls_domain}) is illegal. Should be only UG or TAB4U.")


if __name__ == '__main__':
    path = sys.argv[1]
    domain = sys.argv[2]
    check_path(path)
    check_domain(domain)
    if os.path.isdir(path):
        produce_pdfs(path, domain)
    elif os.path.isfile(path):
        produce_pdf(path, domain)
    print('DONE!\nExiting...')
