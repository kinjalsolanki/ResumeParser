import os
import logging
class FileObject(object):
    def __init__(self):
        self.extn = None
        self.data = None
        self.id = None
        self.error = None
       
    @staticmethod 
    def writeFileToDisk(id, extn, decodedFileContent):
        logging.info("writeFileToDisk STARTS")
        fileName = id + "." + extn
        filePath = os.path.abspath(__file__ +  '/../../../../../temp/' + fileName)
        f= open(filePath,"wb+")
        f.write(decodedFileContent)
        f.close()
        logging.info("writeFileToDisk ENDS")
        return fileName
