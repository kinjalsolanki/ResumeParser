from com.service.parser.core.ParseResume import ParseResume
from com.service.parser.core.StoreResume import StoreResume
from com.service.parser.core.ParseBulkResume import ParseBulkResume
class ParserRequestFactory():
    @staticmethod
    def getInstance(requestType):
        if requestType == "1":
            return ParseResume()
        if requestType == "2":
            return StoreResume()
        if requestType  == "3":
            return ParseBulkResume()
        return None