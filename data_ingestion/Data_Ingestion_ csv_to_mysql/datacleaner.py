#from constants import*
import mysql.connector
from mysql.connector import Error

# Trim whitespace
class DataCleaner(object):
    @classmethod
    def trim_all_columns(cls,df):
        trim_strings = lambda x: x.strip() if isinstance(x, str) else x
        return df.applymap(trim_strings)

def connect ():
        """Testing Connection to MySQL database """
        conn = None

        if conn.is_connected():
                print('Connected to MySQL database')

        else:
            print('not connected')



