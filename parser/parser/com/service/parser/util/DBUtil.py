import mysql.connector
from mysql.connector import Error
import configparser
import os
from com.service.parser.core.FilesFromDB import FilesFromDB
import logging


class DBUtil():
    @staticmethod
    def openConnection():
        logging.info("openConnection STARTS")
        logging.debug("Reading DB config")
        config = configparser.ConfigParser()
        
        fileName = os.path.abspath(__file__ +  '/../../../../../config/config.ini')
        config.read(fileName)
        
        hostname = config['database']['host']
        db = config['database']['dbname']
        username = config['database']['username']
        password = config['database']['password']
        
        try:
            logging.debug("connecting to DB")
            conn = mysql.connector.connect(host=hostname,
                                           database=db,
                                           user=username,
                                           password=password,port=3306)
            if conn.is_connected():
                logging.debug("DB Connected")
                logging.info("openConnection ENDS")
                return conn
     
        except Error as e:
            logging.error("Could not connect to DB. Exception : ", e.message )
            
        return None
        
    @staticmethod
    def storeResumeInDB(fileObj):
        logging.info("storeResumeInDB STARTS")
        conn = DBUtil.openConnection()
        if(conn is None):
            return "Could not connect to database"
        
        try:
            query = "INSERT INTO ResumeStorage(id,file_content,file_extn) " \
                    "VALUES(%s,%s,%s)"
            args = (fileObj["id"], fileObj["data"], "txt")
            logging.info("Executing Query")
            cursor = conn.cursor()
            cursor.execute(query, args)
            conn.commit()
            
        except Error as e:
            logging.error("Could not execute query. Exception : ", e.message )
            return "could not execute query"
        
        finally:
            logging.info("storeResumeInDB ENDS")
            cursor.close()
            conn.close()
        
    @staticmethod
    def getAllResumesFromDB():
        logging.info("getALlResumesFromDB STARTS")
        conn = DBUtil.openConnection()
        filesFromDB = []
        if(conn is None):
            return "Could not connect to database"
        
        try:
            query = "SELECT id,file_content,file_extn FROM ResumeStorage;"
            cursor = conn.cursor()
            logging.info("executing query")
            cursor.execute(query)
            allFiles = cursor.fetchall()
            
            for id, file_content, file_extn in allFiles:
                fileFromDB = FilesFromDB()
                fileFromDB.id = id
                fileFromDB.data = file_content
                fileFromDB.extn= file_extn
                filesFromDB.append(fileFromDB)
        except Error as e:
            logging.error("Could not execute query. Exception : ", e.message )
            return "could not execute query"
        
        finally:
            logging.info("getALlResumesFromDB ENDS")
            cursor.close()
            conn.close()
        return filesFromDB
    
    @staticmethod
    def deleteResumeFromDB(id):
        logging.info("deleteResumeFromDB STARTS")
        conn = DBUtil.openConnection()
        if(conn is None):
            return "Could not connect to database"
        
        try:
            logging.info("executing query")
            query = "DELETE FROM ResumeStorage WHERE id = %s"            
            cursor = conn.cursor()
            cursor.execute(query, (id,))
            conn.commit()
            
        except Error as e:
            logging.error("Could not execute query. Exception : ", e.message )
            return "could not execute query"
        
        finally:
            logging.info("deleteResumeFromDB ENDS")
            cursor.close()
            conn.close()
