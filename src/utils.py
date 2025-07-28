from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.diagnostic import acorr_ljungbox
import matplotlib.pyplot as plt

def adf_test(series):
    result = adfuller(series)
    return result[0], result[1]
def ljung_box_test(residuals, lags=10):
    return {
        'residuals': acorr_ljungbox(residuals, lags=[lags], return_df=True),
        'squared': acorr_ljungbox(residuals**2, lags=[lags], return_df=True)
    }

def plot_volatility(volatility_series):
    plt.figure(figsize=(10,5))
    plt.plot(volatility_series, label='Conditional Volatility')
    plt.title("GARCH Estimated Volatility")
    plt.xlabel("Time")
    plt.ylabel("Volatility (%)")
    plt.legend()
    plt.show()
