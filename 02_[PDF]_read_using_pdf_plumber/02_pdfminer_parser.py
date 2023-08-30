#!/usr/bin/env python

import sys
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from io import StringIO 
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter

class MyParser(object):
    def __init__(self, pdf):
        ## Snipped adapted from Yusuke Shinyamas 
        #PDFMiner documentation
        # Create the document model from the file
        parser = PDFParser(open(pdf, 'rb'))
        document = PDFDocument(parser)
        # Try to parse the document
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        # Create a PDF resource manager object 
        # that stores shared resources.
        rsrcmgr = PDFResourceManager()
        # Create a buffer for the parsed text
        retstr = StringIO()
        # Spacing parameters for parsing
        laparams = LAParams()

        # Create a PDF device object
        device = TextConverter(rsrcmgr, retstr, 
                               laparams = laparams)
        # Create a PDF interpreter object
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        # Process each page contained in the document.
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
        
        self.records            = []
        
        lines = retstr.getvalue().splitlines()
        for line in lines:
            self.handle_line(line)
    
    def handle_line(self, line):
        # Customize your line-by-line parser here
        self.records.append(line)

if __name__ == '__main__':
    filename = 'resources/pdf_files/Die_vier_Jahreszeiten.pdf'
    p = MyParser(filename)
    print( '\n'.join(p.records))