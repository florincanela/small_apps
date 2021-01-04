import PyPDF2
from sys import argv

# pdf_file = argv[1]
# wtr = argv[2]

pdf_file = '../modified_pdf_files/merged_pdf.pdf'
wtr = 'pdf_files/wtr.pdf'

def func(pdf, wtrm):
    with open(pdf, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        with open(wtrm, 'rb') as watermark:
            wtr1 = PyPDF2.PdfFileReader(watermark)
            writer = PyPDF2.PdfFileWriter()
            for i in range(reader.numPages):
                pdf_file1 = reader.getPage(i)
                wtr_file = wtr1.getPage(0)
                pdf_file1.mergePage(wtr_file)
                writer.addPage(pdf_file1)

            with open('test/1st_try.pdf', 'wb') as first_try:
                writer.write(first_try)


if __name__ == '__main__':
    func(pdf_file, wtr)


