import logging
import logging.config
import os

class LoggerUtil():
    @staticmethod
    def getLogger(name):
        logFile = os.path.abspath(__file__ +  '/../../../../../config/log.conf')
        logging.config.fileConfig(logFile)
