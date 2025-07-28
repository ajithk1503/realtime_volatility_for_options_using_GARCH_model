import time
import matplotlib.pyplot as plt
import pandas as pd

from simulate_feed import load_returns
from garch_model import *
from logger import init_logger, log_forecast

# Load data
returns = load_returns()
window_size = 100
steps = 30
init_logger()

# Live plotting setup
plt.ion()
fig, ax = plt.subplots()
vol_forecasts = []

# Real-time simulation loop
for i in range(window_size, window_size+ steps):
    window_data = returns[i - window_size:i]
    forecast_vol = update_garch(window_data)
    vol_forecasts.append(forecast_vol)

    log_forecast(i, forecast_vol)

    ax.clear()
    ax.plot(vol_forecasts, label='Forecast Volatility')
    ax.set_title('Real-Time GARCH Volatility Forecast')
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Volatility (%)')
    ax.legend()
    plt.pause(0.5)
    # time delay to simulate real-time feed (2sec)
    time.sleep(2) 