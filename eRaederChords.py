from ChordsSiteList import ChordsSiteList

def main():
    urls_file_path = 'urls.txt'
    destination_pdf_path = 'Chords.pdf'
    chords_site_list = ChordsSiteList(urls_file_path)
    chords_site_list.sort()
    chords_site_list.save_to_pdf(destination_pdf_path)


if __name__=="__main__":
    main()
