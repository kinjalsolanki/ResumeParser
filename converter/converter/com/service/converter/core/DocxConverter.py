import docx
import os
import logging
class DocxConverter():
    def convert(self, fileName):
        logging.info("DocxConverter.convert STARTS")
        fileName = os.path.abspath(__file__ +  '/../../../../../temp/' + fileName)
        
        doc = docx.Document(fileName)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        os.remove(fileName)
        logging.info("DocxConverter.convert ENDS")
        return '\n'.join(fullText)
