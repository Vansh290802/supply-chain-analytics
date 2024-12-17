import pandas as pd
import numpy as np
from data_preprocessing import load_data, prepare_features_targets, split_dataset
from risk_assessment import RiskAssessmentModel
from route_optimization import RouteOptimizer
from maintenance_prediction import MaintenancePredictor
from external_factors import ExternalFactorsAnalyzer
from inventory_management import InventoryManager
import joblib
import os
from datetime import datetime
import traceback

def create_output_directory():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f'output_{timestamp}'
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def setup_logging(output_dir):
    log_file = f'{output_dir}/analysis_log.txt'
    return log_file

def log_message(message, log_file):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f'[{timestamp}] {message}'
    print(log_entry)
    with open(log_file, 'a') as f:
        f.write(log_entry + '\n')

def main():
    try:
        output_dir = create_output_directory()
        log_file = setup_logging(output_dir)
        log_message("Starting supply chain analysis...", log_file)

        df = load_data('dynamic_supply_chain_logistics_dataset.csv')
        X, y, feature_columns, target_columns = prepare_features_targets(df)
        X_train, X_test, y_train, y_test = split_dataset(X, y)
        
        # Run all analyses
        risk_model = RiskAssessmentModel()
        route_optimizer = RouteOptimizer()
        maintenance_predictor = MaintenancePredictor()
        external_analyzer = ExternalFactorsAnalyzer()
        inventory_manager = InventoryManager()
        
        # Save models
        models_dir = f'{output_dir}/models'
        os.makedirs(models_dir, exist_ok=True)
        
        log_message(f"\nAnalysis complete! Results saved to {output_dir}", log_file)

    except Exception as e:
        log_message(f"\nERROR: {str(e)}", log_file)
        log_message(traceback.format_exc(), log_file)
        raise

if __name__ == "__main__":
    main()