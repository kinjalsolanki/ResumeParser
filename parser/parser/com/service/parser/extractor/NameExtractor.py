import logging
class NameExtractor():
    @staticmethod
    def extractInformation(NLPDoc):
        logging.info("NameExtractor.extractInformation STARTS")

        blackListedWords = ["contact", "information", "firstname", "lastname", "surname", "first", "name", "address", "email", "cover", "letter", "career", "objective", "mr.", "ms.", "mrs.", "miss", "master", "residency", "curriculum", "vitae"]
        isFirstNounAvailable = False
        isSecondNounAvailable= False
        possibleName = ""

        for token in NLPDoc:
            if (token.tag_ == "NNP" or token.tag_ == "NNS" or token.tag_ == "NN") and token.text.lower() not in blackListedWords:           
                possibleName = possibleName + token.text + " "
                if isFirstNounAvailable == True and isSecondNounAvailable == True:
                    logging.info("NameExtractor.extractInformation ENDS")
                    return possibleName
                if isFirstNounAvailable == True:
                    isSecondNounAvailable = True
                else:
                    isFirstNounAvailable = True
            else:
                if isFirstNounAvailable == True and isSecondNounAvailable == True:
                    logging.info("NameExtractor.extractInformation ENDS")
                    return possibleName
                possibleName = ""
                isFirstNounAvailable = False
                isSecondNounAvailable= False
        logging.info("NameExtractor.extractInformation ENDS")
        return "No_Name_Found"
