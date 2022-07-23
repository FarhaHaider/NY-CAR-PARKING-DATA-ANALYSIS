
from db_connect import *
# This part contains code for creation of table in the database


# Create nyparking class to create the table with its schema

class nyparking(Base):
    __tablename__="nyparking"
    id= Column(Integer,primary_key=True,autoincrement=True)
    Summons_Number=Column(BIGINT)
    Plate_ID=Column(TEXT)
    Registration_State=Column(TEXT)
    Plate_Type=Column(TEXT)
    Issue_Date=Column(TEXT)
    Violation_Code=Column(TEXT)
    Vehicle_Body_Type=Column(TEXT)
    Vehicle_Make=Column(TEXT)
    Issuing_Agency=Column(TEXT)
    Street_Code1=Column(TEXT)
    Street_Code2=Column(TEXT)
    Street_Code3=Column(TEXT)
    Vehicle_Expiration_Date=Column(TEXT)
    Violation_Location=Column(TEXT)
    Violation_Precinct=Column(TEXT)
    Issuer_Precinct=Column(TEXT)
    Issuer_Code=Column(TEXT)
    Issuer_Command=Column(TEXT)
    Issuer_Squad=Column(TEXT)
    Violation_Time=Column(TEXT)
    Time_First_Observed=Column(TEXT)
    Violation_County=Column(TEXT)
    Violation_In_Front_Of_Or_Opposite=Column(TEXT)
    House_Number=Column(TEXT)
    Street_Name=Column(TEXT)
    Intersecting_Street=Column(TEXT)
    Date_First_Observed=Column(TEXT)
    Law_Section=Column(TEXT)
    Sub_Division=Column(TEXT)
    Violation_Legal_Code=Column(TEXT)
    Days_Parking_In_Effect=Column(TEXT)
    From_Hours_In_Effect=Column(TEXT)
    To_Hours_In_Effect=Column(TEXT)
    Vehicle_Color=Column(TEXT)
    Unregistered_Vehicle=Column(TEXT)
    Vehicle_Year=Column(TEXT)
    Meter_Number=Column(TEXT)
    Feet_From_curb=Column(TEXT)
    Violation_Post_Code=Column(TEXT)
    Violation_Description=Column(TEXT)
    No_Standing_or_Stopping_Violation=Column(TEXT)
    Hydrant_Violation=Column(TEXT)
    Double_Parking_Violation=Column(TEXT)
    Latitude=Column(TEXT)
    Longitude=Column(TEXT)
    Community_Board=Column(TEXT)
    Community_Council=Column(TEXT)
    Census_Tract=Column(TEXT)
    BIN=Column(TEXT)
    BBL=Column(TEXT)
    NTA=Column(TEXT)

# Function to create table
    def create_table(Base):
        Base.metadata.create_all(engine)

    create_table(Base)