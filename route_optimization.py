import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class RouteOptimizer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.cluster_model = KMeans(n_clusters=5, random_state=42)
    
    def optimize_routes(self, df):
        route_features = ['Traffic_Congestion_Level', 'Weather_Condition_Severity', 
                         'Route_Risk_Level', 'ETA_Variation', 'Port_Congestion_Level']
        X = self.scaler.fit_transform(df[route_features])
        clusters = self.cluster_model.fit_predict(X)
        df['Route_Cluster'] = clusters
        return self.analyze_clusters(df)
    
    def analyze_clusters(self, df):
        cluster_analysis = df.groupby('Route_Cluster').agg({
            'Traffic_Congestion_Level': 'mean',
            'Weather_Condition_Severity': 'mean',
            'Route_Risk_Level': 'mean',
            'ETA_Variation': 'mean',
            'Delay_Probability': 'mean'
        }).round(3)
        return cluster_analysis