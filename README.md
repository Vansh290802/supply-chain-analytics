# Supply Chain Analytics System

## Overview
A comprehensive supply chain operations analysis system that leverages machine learning for optimizing logistics efficiency and risk management.

## Features
- **Risk Assessment**: Predictive modeling for supply chain disruptions
- **Route Optimization**: Delivery route analysis and optimization
- **Maintenance Prediction**: Vehicle maintenance forecasting
- **External Factors Analysis**: Weather and traffic impact analysis
- **Inventory Management**: Warehouse optimization

## Dataset Information
The system analyzes logistics data from January 2021 to January 2024, including:
- Vehicle tracking data (GPS, fuel consumption)
- Warehouse metrics (inventory levels, equipment availability)
- External conditions (weather, traffic, port congestion)
- Performance indicators (delivery times, order fulfillment)
- Risk metrics (supplier reliability, cargo conditions)

## Project Structure
```
supply-chain-analytics/
├── data_preprocessing.py     # Data cleaning and preparation
├── risk_assessment.py       # Risk analysis models
├── route_optimization.py    # Route optimization
├── maintenance_prediction.py # Maintenance forecasting
├── external_factors.py      # External impact analysis
├── inventory_management.py  # Inventory optimization
├── main.py                 # Main execution script
├── requirements.txt        # Dependencies
└── Dockerfile             # Container configuration
```

## Installation

### Using Docker
```bash
# Build the image
docker build -t supply-chain-analytics .

# Run the container
docker run -v $(pwd):/app supply-chain-analytics
```

### Manual Setup
```bash
# Clone repository
git clone https://github.com/Vansh290802/supply-chain-analytics.git
cd supply-chain-analytics

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run analysis
python main.py
```

## Required Data Format
CSV file with columns:
- Timestamp
- Vehicle_GPS_Latitude/Longitude
- Fuel_Consumption_Rate
- ETA_Variation
- Traffic_Congestion_Level
- Warehouse_Inventory_Level
- Loading_Unloading_Time
- Handling_Equipment_Availability
- Order_Fulfillment_Status
- Weather_Condition_Severity
- Port_Congestion_Level
- And more...

## Dependencies
- Python 3.8+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- joblib

## Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Create Pull Request

## License
MIT License