# importing required modules
import PyPDF2
 
filename = 'resources/pdf_files/example.pdf'
#filename = 'resources/pdf_files/Die_vier_Jahreszeiten.pdf'
filename = 'resources/pdf_files/lorem.pdf'
# creating a pdf file object
pdfFileObj = open(filename, 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
print(pdfReader.numPages)
 
# creating a page object
pageObj = pdfReader.getPage(0)
 
# extracting text from page
text = pageObj.extractText()
print(text)
 
# closing the pdf file object
pdfFileObj.close()