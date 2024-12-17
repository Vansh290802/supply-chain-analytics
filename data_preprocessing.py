import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import os
import sys

def standardize_column_names(df):
    """Standardize column names to proper case and format"""
    standard_names = {
        'timestamp': 'Timestamp',
        'vehicle_gps_latitude': 'Vehicle_GPS_Latitude',
        [Rest of the file content...]
    }
    return df
