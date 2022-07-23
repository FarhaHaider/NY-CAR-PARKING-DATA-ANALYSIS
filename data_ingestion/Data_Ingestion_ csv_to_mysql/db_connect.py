
from dotenv import load_dotenv
from sqlalchemy import*
from pathlib import Path
from sqlalchemy .ext.declarative import declarative_base
import os

# This file contains the database connection string
load_dotenv()
env_path=Path('C:/Users/praga/PycharmProjects/pythonProject/config.env')
load_dotenv(dotenv_path=env_path)
mysql_connection = os.getenv("mysql_connection")

#Create baseloader class to create engine and set up connection
Base=declarative_base()
class BaseLoader(object):
    @classmethod
    def get_connection(cls):
        engine = create_engine(mysql_connection)
        conn = engine.connect()
        return engine, conn
base_loader = BaseLoader()
engine, conn = base_loader.get_connection()