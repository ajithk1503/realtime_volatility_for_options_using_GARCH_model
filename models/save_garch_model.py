# save_garch_model.py

import os
import pandas as pd
from arch import arch_model
import joblib

# Step 1: Load processed returns data
# Make sure this file exists and has a 'returns' column
data_path = 'data/processed/NIFTY_500_with_garch_volatility.csv'
df = pd.read_csv(data_path, parse_dates=True, index_col=0)

# Ensure returns column exists
if 'log_return' not in df.columns:
    raise ValueError("Column 'returns' not found in the CSV.")

returns = df['log_return'].dropna()

# Step 2: Fit GARCH(1,1) model
model = arch_model(returns, vol='Garch', p=1, q=1)
result = model.fit(disp='off')

# Step 3: Save model to /models directory
os.makedirs('models', exist_ok=True)
model_path = 'models/garch_model.pkl'
joblib.dump(result, model_path)
print(f"Model saved to {model_path}")

# Step 4: (Optional) Load model back and print summary
loaded_model = joblib.load(model_path)
print("\nLoaded model summary:")
print(loaded_model.summary())
