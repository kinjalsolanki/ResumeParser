from com.service.parser.nlp.NLPProcessor import NLPProcessor
from com.service.parser.extractor.NameExtractor import NameExtractor
from com.service.parser.extractor.ContactDetailExtractor import ContactDetailExtractor
from com.service.parser.extractor.PincodeExtractor import PincodeExtractor
from com.service.parser.core.FilesInformation import FilesInformation
from com.service.parser.extractor.EmailIdExtractor import EmailIdExtractor
import logging
class InformationExtractor():
    @staticmethod
    def getExtractedInformation(fileData):
        logging.info("InformationExtractor.getExtractedInformation STARTS")
        extractedInfo = FilesInformation()
        NLPdoc = NLPProcessor.performNLP(fileData)
        #for token in NLPdoc:
            #logging.info(token.text + "====================" + token.tag_)
        name = NameExtractor.extractInformation(NLPdoc)
        splittedName = name.split(" ")
        extractedInfo.fname = splittedName[0]
        extractedInfo.lname = splittedName[len(splittedName) - 2]
        
        extractedInfo.contactNo = ContactDetailExtractor.extractInformation(NLPdoc)
        extractedInfo.pincode = PincodeExtractor.extractInformation(NLPdoc)
        extractedInfo.email = EmailIdExtractor.extractInformation(NLPdoc)
        logging.info("InformationExtractor.getExtractedInformation ENDS")
        return extractedInfo
