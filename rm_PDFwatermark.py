# import the necessary modules
import PyPDF2

# define the list of PDF files
pdf_files = ['file1.pdf', 'file2.pdf', ..., 'file_X.pdf']

# iterate over the PDF files
for pdf_file in pdf_files:
    # open the PDF file in read-binary mode
    with open(pdf_file, 'rb') as file:
        # create a PDF object
        pdf = PyPDF2.PdfFileReader(file)

    # create a PDF object for the output file
    output_pdf = PyPDF2.PdfFileWriter()

    # iterate over the pages of the PDF
    for page in range(pdf.getNumPages()):
        # get the current page
        current_page = pdf.getPage(page)
        # remove the watermark
        current_page.mergePage(current_page)
        # add the modified page to the output PDF
        output_pdf.addPage(current_page)

    # open the output PDF file in write-binary mode
    with open(pdf_file[:-4] + '_modified.pdf', 'wb') as output:
        # write the modified PDF to the output file
        output_pdf.write(output)
