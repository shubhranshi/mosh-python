# There are several packages to work with PDFs file.
# History of pyPdf, PyPDF2, and PyPDF4
# Although Mosh course is on "pyPDF2", I am using "pyPDF4"

# install pip or pipenv PyPDF4
import PyPDF4

# We use the "with" to open a PDF file. And we open it in the "rb" mode read binary,
# we get a file stream object, so we can use it as a "reader" object with the PyPDF$ package.
with open("first.pdf", "rb") as pdf_file:
    reader = PyPDF4.PdfFileReader(pdf_file)
    # With the reader object we can use several methods. In this case "numPages" returns the number of pages
    print(reader.numPages)
    # With the "getPage" method we can geta page from the PDF. Important, the page count starts at 0
    page = reader.getPage(0)
    # With the page object we can use several other methods. In here "rotateClockwise()" to rotate the page.
    # This is only rotates the page object in memory, and does not modify the original PDF.
    # So we need to write this to a separate PDF file.
    page.rotateClockwise(90)
    writer = PyPDF4.PdfFileWriter() # Here we create the writer object.
    writer.addPage(page) # Here we are adding the page object to our new pdf, in memory.
    with open("rotated.pdf", "wb") as output: # We create a new file and use the "wb" write binary.
        writer.write(output) # we use our writer to write to the new file.

merger = PyPDF4.PdfFileMerger() # To merge pdf we first create a merger object with the  ".PdfFileMerger()"
# Here we are using a list with the PDF file we want to merge. We could iterate over all the PDF in a folder.
file_names = ["first.pdf", "second.pdf"]
for file_name in file_names: # with the for loop we iterate over the list with the PDf files
    merger.append(file_name) # We use the ".append()" method to add each PDF to our merger object in memory.

# With the ".write()" we create a new file in disk from our merge object. Here e named it "combined.pdf"
merger.write("combined.pdf")
