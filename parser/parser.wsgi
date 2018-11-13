activate_this = '/path/to/resume_parser/python3/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/path/to/resume_parser/parser/parser")
from parser.main import app as application
