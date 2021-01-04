import PyPDF2

pdf_file = PyPDF2.PdfFileReader(open('../modified_pdf_files/merged_pdf.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('../pdf_files/wtr.pdf', 'rb'))

writer = PyPDF2.PdfFileWriter()

for i in range(pdf_file.getNumPages()):
    pdf_page = pdf_file.getPage(i)
    wtr = watermark.getPage(0)
    pdf_page.mergePage(wtr)
    writer.addPage(pdf_page)

with open('test/test2.pdf', 'wb') as output:
    writer.write(output)
