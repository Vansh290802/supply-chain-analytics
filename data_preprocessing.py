import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import os
import sys

def standardize_column_names(df):
    """Standardize column names to proper case and format"""
    # Define standard names for all columns
    standard_names = {
        'timestamp': 'Timestamp',
        'vehicle_gps_latitude': 'Vehicle_GPS_Latitude',
        'vehicle_gps_longitude': 'Vehicle_GPS_Longitude',
        'fuel_consumption_rate': 'Fuel_Consumption_Rate',
        'eta_variation_hours': 'ETA_Variation',
        'traffic_congestion_level': 'Traffic_Congestion_Level',
        'warehouse_inventory_level': 'Warehouse_Inventory_Level',
        'loading_unloading_time': 'Loading_Unloading_Time',
        'handling_equipment_availability': 'Handling_Equipment_Availability',
        'order_fulfillment_status': 'Order_Fulfillment_Status',
        'weather_condition_severity': 'Weather_Condition_Severity',
        'port_congestion_level': 'Port_Congestion_Level',
        'shipping_costs': 'Shipping_Costs',
        'supplier_reliability_score': 'Supplier_Reliability_Score',
        'lead_time_days': 'Lead_Time',
        'historical_demand': 'Historical_Demand',
        'iot_temperature': 'IoT_Temperature',
        'cargo_condition_status': 'Cargo_Condition_Status',
        'route_risk_level': 'Route_Risk_Level',
        'customs_clearance_time': 'Customs_Clearance_Time',
        'driver_behavior_score': 'Driver_Behavior_Score',
        'fatigue_monitoring_score': 'Fatigue_Monitoring_Score',
        'disruption_likelihood_score': 'Disruption_Likelihood_Score',
        'delay_probability': 'Delay_Probability',
        'risk_classification': 'Risk_Classification',
        'delivery_time_deviation': 'Delivery_Time_Deviation'
    }
    
    # Create a mapping for the columns that exist in the dataframe
    column_mapping = {
        col: standard_names.get(col.lower(), col) 
        for col in df.columns
    }
    
    # Rename columns
    df = df.rename(columns=column_mapping)
    
    # Remove any duplicate columns (case-insensitive)
    df = df.loc[:, ~df.columns.str.lower().duplicated()]
    
    return df

[Rest of the file content...]