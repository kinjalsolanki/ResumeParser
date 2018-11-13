from com.service.converter.core.PDFConverter import PDFConverter
from com.service.converter.core.DocxConverter import DocxConverter
from com.service.converter.core.DocConverter import DocConverter
class ConverterFactory():
    @staticmethod
    def getInstance(extn):
        if extn.lower() == "pdf":
            return PDFConverter()
        if extn.lower() == "docx":
            return DocxConverter()
        if extn.lower() == "doc":
            return DocConverter()
        return None
        
