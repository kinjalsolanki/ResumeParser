import logging
class EmailIdExtractor():
    @staticmethod
    def extractInformation(NLPDoc):
        logging.info("EmailIdExtractor.extractInformation STARTS")
        for token in NLPDoc:
            if "@" in token.text:
                if "." in token.text:
                    logging.info("EmailIdExtractor.extractInformation ENDS")
                    return token.text
        logging.info("EmailIdExtractor.extractInformation ENDS")
        return ""
