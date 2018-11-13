import spacy
import logging
class NLPProcessor():
    @staticmethod
    def performNLP(fileContent):
        logging.debug("Running NLP cycle")
        nlp = spacy.load('en')
        doc = nlp(fileContent)
        logging.debug("NLP cycle complete")
        return doc
