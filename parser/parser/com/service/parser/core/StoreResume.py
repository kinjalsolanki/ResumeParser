from com.service.parser.util.ConversionUtil import ConversionUtil
from com.service.parser.util.DBUtil import DBUtil
import logging
class StoreResume():
    def __init__(self):
        self.requestType = "2"
        
    def process(self, requestData):
        logging.info("StoreResume.process STARTS")

        convertedFiles = ConversionUtil.getConvertedFiles(requestData)
        for fileObj in convertedFiles["files"]:
            if not fileObj["error"]:
                error = DBUtil.storeResumeInDB(fileObj)
                if error:
                    logger.info("Some exception occured: process ENDS")
                    return '{"error": "' + error + '"}'
        logging.info("StoreResume.process ENDS")
        return '{"status:" : "success"}'
