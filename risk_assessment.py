import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.metrics import classification_report, mean_squared_error
import joblib

class RiskAssessmentModel:
    def __init__(self):
        self.disruption_model = RandomForestRegressor(random_state=42)
        self.risk_classifier = RandomForestClassifier(random_state=42)
        
    def train(self, X_train, y_train):
        print("Training risk assessment models...")
        if 'Disruption_Likelihood_Score' in y_train.columns:
            self.disruption_model.fit(X_train, y_train['Disruption_Likelihood_Score'])
        if 'Risk_Classification' in y_train.columns:
            self.risk_classifier.fit(X_train, y_train['Risk_Classification'])
    
    def predict(self, X):
        predictions = {}
        if hasattr(self.disruption_model, 'feature_importances_'):
            predictions['disruption_likelihood'] = self.disruption_model.predict(X)
        if hasattr(self.risk_classifier, 'feature_importances_'):
            predictions['risk_classification'] = self.risk_classifier.predict(X)
        return predictions