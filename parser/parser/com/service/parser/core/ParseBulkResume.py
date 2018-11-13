from com.service.parser.util.DBUtil import DBUtil
import base64
from com.service.parser.extractor.InformationExtractor import InformationExtractor
from com.service.parser.core.ParserData import ParserData
import jsonpickle
import logging
class ParseBulkResume:
    def __init__(self):
        self.requestType = "3"
        
    def process(self, requestData):
        logging.info("ParseBulkResume.process STARTS")
        logging.info("Fetching all resumes from DB")
        allResumes = DBUtil.getAllResumesFromDB()
        outputData = ParserData()
        if type(allResumes) is list:
            logging.info("%s resumes fetched from the DB" , len(allResumes))
            for resume in allResumes:
                if resume.extn == "txt":
                    logging.debug("Base64 decoding file data with id %s", resume.id)
                    decodedData =  base64.b64decode(resume.data)
                    fileData = "".join(map(chr, decodedData))
                    logging.debug("extracting information from file data with id %s", resume.id)
                    fileInformation = InformationExtractor.getExtractedInformation(fileData)
                    fileInformation.id = resume.id
                    outputData.files.append(fileInformation)
                    DBUtil.deleteResumeFromDB(resume.id)
                else:
                    logging.info("extension other than txt found from DB")
            logging.info("ParseBulkResume.process ENDS")
            return jsonpickle.encode(outputData, unpicklable=False)
        else:
            return '{"error": "' + allResumes + '"}'
