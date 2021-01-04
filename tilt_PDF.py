import PyPDF2

with open('pdf_files/dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('modified_pdf_files/tilted_dummy.pdf', 'wb') as tilted_file:
        writer.write(tilted_file)
        print('done!')