import csv
import os

def init_logger(path='outputs/logs/vol_forecasts.csv'):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['step', 'forecast_volatility'])

def log_forecast(step, forecast_vol, path='outputs/logs/vol_forecasts.csv'):
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([step, forecast_vol])

