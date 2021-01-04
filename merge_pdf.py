from sys import argv
import PyPDF2

inputs = argv[1:]

def merge_func(input):
    merger = PyPDF2.PdfFileMerger()
    for x in input:
        merger.append(x)
    merger.write('modified_pdf_files/merged_pdf.pdf')

if __name__ == '__main__':
    merge_func(inputs)
    print('done!')