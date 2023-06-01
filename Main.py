from TabletPDFWriter import TabletPDFWriter
import os


def produce_pdfs(urls_dir, domain):
    for urls_file in os.listdir(urls_dir):
        filepath = os.path.join(urls_dir, urls_file)
        if not os.path.isfile(filepath):
            continue
        tablet_chord_writer = TabletPDFWriter(filepath, domain)
        file_name = os.path.splitext(os.path.basename(filepath))[0]
        pdf_file_path = 'Output/'+file_name+'.pdf'
        tablet_chord_writer.make_pdf(pdf_file_path)


if __name__ == '__main__':

    ug_urls_dir = './URLs/UG'
    tab4u_urls_dir = './URLs/TAB4U'

    produce_pdfs(ug_urls_dir, 'UG')
    produce_pdfs(tab4u_urls_dir, 'TAB4U')
    print('DONE!')
