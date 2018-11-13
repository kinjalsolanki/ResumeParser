import configparser
import jsonpickle
from flask.globals import request
import os
import requests
import json
import logging
class ConversionUtil:
    @staticmethod
    def getConvertedFiles(data):
        logging.info("getConverterdFiles STARTS")
        config = configparser.ConfigParser()
        
        fileName = os.path.abspath(__file__ +  '/../../../../../config/config.ini')
        config.read(fileName)
        
        converterUrl = config['converter']['url']
        logging.info("converter service URL: %s", converterUrl)
        
        converterData = jsonpickle.encode(data, unpicklable=False)

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        convertedFiles = requests.post(converterUrl, data=converterData, headers=headers)
        responseData = json.loads(convertedFiles.text)
        logging.info("getConverterdFiles ENDS")
        return responseData
