import sys
from flask import Flask
import jsonpickle
from com.service.converter.core.ConverterFactory import ConverterFactory
from flask.globals import request
import json
import base64
from com.service.converter.core.FileObject import FileObject
from com.service.converter.core.ConverterData import ConverterData
from com.service.converter.util.LoggerUtil import LoggerUtil
import logging
app = Flask(__name__)

@app.route('/convert', methods=['GET', 'POST'])
def convert_to_text():
    LoggerUtil.getLogger(__name__)
    logging.info("received request for conversion")
    jsonRequestData = request.get_json(force=True)
    reqData = json.dumps(jsonRequestData)
    logging.debug("getting JSON request data")

    converterRequestData = jsonpickle.decode(reqData)
    
    outputData = ConverterData()
    for fileObj in converterRequestData["files"]:
        fileOutputObj = FileObject()
        fileOutputObj.extn = "txt"
        fileOutputObj.id = fileObj["id"]
        logging.debug("decoding base64 file data")

        decodedData =  base64.b64decode(fileObj["data"])
        
        extnConverter = ConverterFactory.getInstance(fileObj["extn"])
        if extnConverter ==  None:
            logging.error("unsupported extension %s" , fileObj["extn"])
            fileOutputObj.error = "Extension not supported"
        else:
            logging.debug("writing file to disk")
            fileName = FileObject.writeFileToDisk(fileObj["id"], fileObj["extn"], decodedData)
            logging.debug("converting file to txt")
            textData = extnConverter.convert(fileName)
            fileOutputObj.data = base64.b64encode(bytes(textData, "utf-8")).decode('ascii')
        outputData.files.append(fileOutputObj)
    logging.info("returning response")
    text = jsonpickle.encode(outputData, unpicklable=False)
    logging.info(text)
    return jsonpickle.encode(outputData, unpicklable=False)

@app.route('/')
def hello():
    return "Conversion service running"

if __name__ == '__main__':
    app.run()
