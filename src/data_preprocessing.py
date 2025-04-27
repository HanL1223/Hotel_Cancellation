
import warnings
import logging

warnings.filterwarnings("ignore")

# Libraries to help with reading and manipulating data
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

#For date manipulation
from datetime import datetime


# Library to split data
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_data(filepath: str) -> pd.DataFrame:
    """Load raw data with validation checks."""
    try:
        df = pd.read_csv(filepath)
        logger.info(f"Data loaded. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        logger.error(f"File not found at {filepath}")
        raise

def data_cleaning(df):
    """
    Data cleanning as idenfied in EDA
    """
    #1.Duplication
    df = df.drop_duplicate()
    #2.Remove 2018-02-29
    df.drop(df[(df['arrival_year']==2018)&(df['arrival_month']==2)&(df['arrival_date']==29)].index,axis = 0,inplace = True)
    #3. Because Room Type 2,3,5,7 contains very less information, we can combine them as 1 category 'other'
    # We will combine Room_Type 2,3,5 and 7
    # Replace multiple room types with "Others" in one operation
    df.loc[df['room_type_reserved'].isin(["Room_Type 2", "Room_Type 3", "Room_Type 5", "Room_Type 7"]), 
        'room_type_reserved'] = "Others"
    logger.info(f"Data cleaned. New shape: {df.shape}")
    return df


def feature_engineering(df):
    # 1. Convert months to 4 seasons
    seasons_map = {
        1: "Winter", 2: "Winter", 3: "Spring", 
        4: "Spring", 5: "Spring", 6: "Summer",
        7: "Summer", 8: "Summer", 9: "Fall",
        10: "Fall", 11: "Fall", 12: "Winter"
    }
    df["arrival_season"] = df["arrival_date_month"].map(seasons_map)
    #1 Encode all attributes
    cat_col = df.select_dtypes(['category','object']).columns
    for col in cat_col:
        df[col] = df[col].astype(str).str.strip()  # remove leading/trailing spaces

    # Then do one-hot encoding and force dtype=int
    df = pd.get_dummies(df, columns=cat_col, dtype=int)
    logger.info("Feature engineering completed")
    return df
