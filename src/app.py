import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
import joblib
import numpy as np

from simulate_feed import load_returns
from garch_model import update_garch
from logger import log_forecast

st.set_page_config(layout="wide")
st.title("📈 Real-Time GARCH Volatility Forecasting")

# Config
window_size = 100
forecast_steps = st.slider("Number of steps to forecast", 10, 100, 30)
data_path = 'data/processed/NIFTY_500_with_garch_volatility.csv'
model_path = 'models/garch_model.pkl'

# Load data
returns = load_returns(data_path)
returns = returns.dropna().reset_index(drop=True)

# Initialize forecast storage
vol_forecasts = []
forecast_indices = []

# Streamlit elements
plot_placeholder = st.empty()
log_placeholder = st.empty()
progress_bar = st.progress(0)

# Real-time simulation loop
for step in range(window_size, window_size + forecast_steps):
    window_data = returns[step - window_size:step]
    forecast_vol = update_garch(window_data)
    
    vol_forecasts.append(forecast_vol)
    forecast_indices.append(step)

    log_forecast(step, forecast_vol)

    # Plot update
        # Plot update
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(forecast_indices, vol_forecasts, label='Forecast Volatility', color='orange')
    ax.set_title("Real-Time GARCH Volatility Forecast")
    ax.set_xlabel("Time Step")
    ax.set_ylabel("Volatility (%)")
    ax.legend()
    plot_placeholder.pyplot(fig)
    plt.close(fig)

    log_placeholder.markdown(f"**Step {step}:** Forecast Volatility = `{forecast_vol:.4f}`")
    progress_bar.progress((step - window_size + 1) / forecast_steps)

    time.sleep(2)

st.success("✅ Forecasting Complete!")
