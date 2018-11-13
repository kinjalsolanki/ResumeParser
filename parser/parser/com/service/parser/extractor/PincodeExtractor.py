import logging
class PincodeExtractor():
    @staticmethod
    def extractInformation(NLPDoc):
        logging.info("PinCodeExtractor.extractInformation STARTS")

        for token in NLPDoc:
            possibleVal = token.text
                
            if "-" in token.text:
                splitted = token.text.split("-")
                possibleVal = splitted[len(splitted)- 1]
            if ":" in token.text:
                splitted = token.text.split(":")
                possibleVal = splitted[len(splitted)- 1]
            if "," in token.text:
                splitted = token.text.split(",")
                possibleVal = splitted[len(splitted)- 1]
            if len(possibleVal) == 6 and possibleVal.isdigit():
                    logging.info("PinCodeExtractor.extractInformation ENDS")
                    return possibleVal

        logging.info("PinCodeExtractor.extractInformation ENDS")
        return ""
