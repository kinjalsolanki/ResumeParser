import sys
from flask import Flask
import jsonpickle
import json
import logging
from com.service.parser.core.ParserRequestFactory import ParserRequestFactory
from flask.globals import request
from com.service.parser.util.LoggerUtil import LoggerUtil
app = Flask(__name__)

@app.route('/')
def hello():
    return "Parser Service Running"

if __name__ == '__main__':
    app.run()

@app.route('/parse', methods=['GET', 'POST'])
def extract_information():
    LoggerUtil.getLogger(__name__)
    logging.info("Received request for parsing")
    jsonRequestData = request.get_json(force=True)
    reqData = json.dumps(jsonRequestData)
    parserRequestData = jsonpickle.decode(reqData)
    logging.info("decoded JSON request data")
    requestObject = ParserRequestFactory.getInstance(parserRequestData["request_type"])
    logging.info("created request instance. Now processing the request")
    extractedInfo = requestObject.process(parserRequestData)
    logging.info("returning the response %s" , extractedInfo)
    return extractedInfo
