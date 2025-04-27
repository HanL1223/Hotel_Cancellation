import pandas as pd
from Pathlib import Path

#Import csv
csv_path = Path('../data/raw/StarHotelsGroup.csv')
raw_data = pd.read_csv(csv_path)

#preprocessing steps

def preprocessing(data):
    """
    Function to preprocess the data as identified during EDA
    1.General removal of duplicate 
    """
    # We will combine summer months (March-August) & winter months (September-February)
    
def feature_eng(data):
    data["arrival_month"] = data["arrival_month"].astype("object")

    data.loc[data.arrival_month==1, "arrival_month"] = "Winter"
    data.loc[data.arrival_month==2, "arrival_month"] = "Winter"
    data.loc[data.arrival_month==3, "arrival_month"] = "Summer"
    data.loc[data.arrival_month==4, "arrival_month"] = "Summer"
    data.loc[data.arrival_month==5, "arrival_month"] = "Summer"
    data.loc[data.arrival_month==6, "arrival_month"] = "Summer"
    data.loc[data.arrival_month==7, "arrival_month"] = "Summer"
    data.loc[data.arrival_month==8, "arrival_month"] = "Summer"
    data.loc[data.arrival_month==9, "arrival_month"] = "Winter"
    data.loc[data.arrival_month==10, "arrival_month"] = "Winter"
    data.loc[data.arrival_month==11, "arrival_month"] = "Winter"
    data.loc[data.arrival_month==12, "arrival_month"] = "Winter"

    data["arrival_month"] = data["arrival_month"].astype("category")


    # We will combine Meal Plan 3 with Meal Plan 2
    data["type_of_meal_plan"] = data["type_of_meal_plan"].astype("object")
    data["room_type_reserved"] = data["room_type_reserved"].astype("object")

    data.loc[data.type_of_meal_plan=="Meal Plan 2", "type_of_meal_plan"] = "Not_Meal_Plan 1"
    data.loc[data.type_of_meal_plan=="Meal Plan 3", "type_of_meal_plan"] = "Not_Meal_Plan 1"

    # We will combine Room_Type 2,3,5 and 7
    data.loc[data.room_type_reserved =="Room_Type 2", "room_type_reserved"] = "Others"
    data.loc[data.room_type_reserved =="Room_Type 3", "room_type_reserved"] = "Others"
    data.loc[data.room_type_reserved =="Room_Type 5", "room_type_reserved"] = "Others"
    data.loc[data.room_type_reserved =="Room_Type 7", "room_type_reserved"] = "Others"

    data["type_of_meal_plan"] = data["type_of_meal_plan"].astype("category")
    data["room_type_reserved"] = data["room_type_reserved"].astype("category")