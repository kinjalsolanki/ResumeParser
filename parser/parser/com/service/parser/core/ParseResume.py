from com.service.parser.util.ConversionUtil import ConversionUtil
import base64
from com.service.parser.extractor.InformationExtractor import InformationExtractor
from com.service.parser.core.ParserData import ParserData
import jsonpickle
import logging
class ParseResume():
    def __init__(self):
        self.requestType = "1"
        
    def process(self, requestData):
        logging.info("ParseResume.process STARTS")
        logging.debug("converting files to txt format")
        convertedFiles = ConversionUtil.getConvertedFiles(requestData)
        outputData = ParserData()
        for fileObj in convertedFiles["files"]:
            if not fileObj["error"]:
                decodedData =  base64.b64decode(fileObj["data"])
                fileData = "".join(map(chr, decodedData))
                fileInformation = InformationExtractor.getExtractedInformation(fileData)
                fileInformation.id = fileObj["id"]
                outputData.files.append(fileInformation)
        logging.info("ParseResume.process ENDS")
        return jsonpickle.encode(outputData, unpicklable=False)
