#firstly - pip install PyPDF2

import PyPDF2

pdf_files = ["1.pdf", "2.pdf"] 

merger = PyPDF2.PdfMerger()

for filename in pdf_files:

    pdfFile = open(filename, 'rb') 
    pdfReader = PyPDF2.PdfReader(pdfFile) 
    merger.append(pdfReader)
    pdfFile.close()

merger.write('merged.pdf')

'''
To read a PDF file with Python, you first have to import the PyPDF2 module. 
Next, you need to open the PDF file you want to read using the default Python open method. 
Since PDF files contain data in binary format, the permission for the open() method should be set to rb (read binary). 
Once you open the file, the file handler returned by the open() method is passed to the constructor of the PdfFileReader class of the PyPDF2 module. 
The object of the PdfFileReader class can then be used to read text from a PDF document. 

'''