import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from _io import StringIO
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
import logging
class PDFConverter():
    def convert(self,fileName):
        logging.info("PDFConverter.convert STARTS") 
        resourceManager = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(resourceManager, retstr, codec=codec, laparams=laparams)
        
        
        filename = os.path.abspath(__file__ +  '/../../../../../temp/' + fileName)
        
        fp = open(filename,"rb")
        interpreter = PDFPageInterpreter(resourceManager, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
    
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, 
                                      password=password,caching=caching, 
                                      check_extractable=True):
            interpreter.process_page(page)
    
        text = retstr.getvalue()
    
        fp.close()
        device.close()
        retstr.close()
        os.remove(filename)
        logging.info("PDFConverter.convert ENDS")
        return text
