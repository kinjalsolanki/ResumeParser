import logging
class ContactDetailExtractor():
    @staticmethod
    def extractInformation(NLPDoc):
        logging.info("ContactDetailExtractor.extractInformation STARTS")
        possibleContactDetail = []
        separatedContactNumber = ""
        for token in NLPDoc:
            if "," in token.text and len(token.text) > 10:
                splitted = token.text.split(",")
                for splittedNumber in splitted:
                    if len(splittedNumber) >= 10 and splittedNumber.isdigit():
                        possibleContactDetail.append(splittedNumber)
            if "/" in token.text and len(token.text) > 10:
                splitted = token.text.split("/")
                for splittedNumber in splitted:
                    if len(splittedNumber) >= 10 and splittedNumber.isdigit():
                        possibleContactDetail.append(splittedNumber)
            if "-" in token.text and len(token.text) > 10:
                splitted = token.text.split("-")
                for splittedNumber in splitted:
                    if len(splittedNumber) >= 10 and splittedNumber.isdigit():
                        possibleContactDetail.append(splittedNumber)

            if token.tag_ == "CD":
                if len(token.text) >= 10 and token.text.isdigit():
                    possibleContactDetail.append(token.text)
                elif len(token.text) + len(separatedContactNumber) <= 12 and token.text.isdigit():
                    separatedContactNumber = separatedContactNumber + token.text
            else:
                if len(separatedContactNumber) == 10 or len(separatedContactNumber) == 12:
                    possibleContactDetail.append(separatedContactNumber)
                separatedContactNumber = ""
        logging.info("ContactDetailExtractor.extractInformation ENDS")
        return possibleContactDetail    
