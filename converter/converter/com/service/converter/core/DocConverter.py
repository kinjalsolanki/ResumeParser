from subprocess import Popen, PIPE
import os
import logging
class DocConverter():
    def convert(self, fileName):
        logging.info("DocConverter.convert STARTS")
        fileName = os.path.abspath(__file__ +  '/../../../../../temp/' + fileName)
        cmd = ['/root/bin/antiword', fileName]
        p = Popen(cmd, stdout=PIPE)
        stdout, stderr = p.communicate()
        fullText = stdout.decode('ascii', 'ignore')
        os.remove(fileName)
        logging.info("DocConverter.convert ENDS")     
        return fullText
