import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv
load_dotenv()




class connectionDb():

    @staticmethod
    def connect():
        db_host = (os.getenv("DATABASE_HOST"))
        db_port = (os.getenv("DATABASE_PORT"))
        db_user = (os.getenv("DATABASE_USER"))
        db_pass = (os.getenv("DATABASE_PASSWORD"))
        db_db = (os.getenv("DATABASE_DB"))

        mydb = pymysql.connect(host=db_host, port=int(db_port), user=db_user, passwd=db_pass, db=db_db, cursorclass=pymysql.cursors.DictCursor)
        return mydb
    