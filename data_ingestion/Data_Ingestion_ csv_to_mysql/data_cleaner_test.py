
import pandas as pd
from datacleaner import*
import mysql.connector
from mysql.connector import Error


class TestDataCleaner(object):
    cleaner_dict_data=[{'Summons_Number':1283294138,'Plate_ID':'GBB9093','Registration_State':'NY','Plate_Type':'PAS','Issue_Date':'08-04-2013',
                        'Violation_Code':'46','Vehicle_Body_Type':'SUBN','Vehicle_Make':'AUDI',
    'Issuing_Agency':' P ',
    'Street_Code1':'37250',
    'Street_Code2':'13610',
    'Street_Code3':'21190',
    'Vehicle_Expiration_Date':'20140831',
    'Violation_Location':'33',
    'Violation_Precinct':'33',
    'Issuer_Precinct':'33',
    'Issuer_Code':'921043',
    'Issuer_Command':'33',
    'Issuer_Squad':'0',
    'Violation_Time':'0752A',
    'Time_First_Observed':'',
    'Violation_County':'',
    'Violation_In_Front_Of_Or_Opposite':'F',
    'House_Number':'712',
    'Street_Name':'W 175 ST',
    'Intersecting_Street':'',
    'Date_First_Observed':'0',
    'Law_Section':'408',
    'Sub_Division':'F1',
    'Violation_Legal_Code':'',
    'Days_Parking_In_Effect':'BBBBBBB',
    'From_Hours_In_Effect':'ALL',
    'To_Hours_In_Effect':'ALL',
    'Vehicle_Color':'GY',
    'Unregistered_Vehicle':'0',
    'Vehicle_Year':'2013',
    'Meter_Number':'-',
    'Feet_From_curb':'0',
    'Violation_Post_Code':'',
    'Violation_Description':'',
   'No_Standing_or_Stopping_Violation':'',
    'Hydrant_Violation':'',
    'Double_Parking_Violation':'',
    'Latitude':'',
    'Longitude':'',
    'Community_Board':'',
    'Community_Council':'',
    'Census_Tract':'',
    'BIN':'',
    'BBL':'',
    'NTA':''}]

    cleaner_test_df=pd.DataFrame.from_dict(data=cleaner_dict_data)
    def test_trim_in_cleaner(self):
        # Test after trimming all columns
        print("Running test_trim_in_cleaner")
        trimmed_data_df = DataCleaner.trim_all_columns(self.cleaner_test_df)

        trimmed_issuing_agency = trimmed_data_df[trimmed_data_df['Summons_Number'] == 1283294138].iloc[0][
            'Issuing_Agency']
        assert trimmed_issuing_agency =='P'
        print("test_trim passed")

    def test_db_connection(self):
        print("Running db connection")
        conn = mysql.connector.connect(host='13.72.71.183',
                                       database='de_ny_cp_team1',
                                       user='training',
                                       password='training')
        print("db connection test passed")




if __name__ == "__main__":
    P = TestDataCleaner()
    P.test_trim_in_cleaner()

    #print("test_trim passed")
    P.test_db_connection()
    #print("db connection test passed")


