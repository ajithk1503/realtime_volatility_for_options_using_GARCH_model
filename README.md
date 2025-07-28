# 📈 Real-Time GARCH Volatility Forecasting

This project simulates a real-time financial forecasting pipeline using a GARCH (Generalized Autoregressive Conditional Heteroskedasticity) model. It processes stock returns, forecasts volatility, logs predictions, and visualizes them dynamically using **Streamlit**.

---

## 🧠 Model

- **Model Type:** GARCH(1,1)
- **Library Used:** `arch` package
- **Inputs:** Log returns of financial time series (e.g., NIFTY 500)
- **Output:** One-step-ahead forecast of volatility
- **Persistence:** Trained model is saved as `models/garch_model.pkl`
- **Usage:** `garch_model.py` contains methods to fit, update, and forecast using the model
- **Refitting Strategy:** Incrementally updated as new data becomes available (online-style simulation)

---

### App Link : [Real-Time GARCH Volatility Forecasting](https://volatility-for-options-using-garch.streamlit.app/)

## ✅ Features

- 📡 **Real-time Simulation**  
  Simulates a real-time data feed using historical log return data.

- 📈 **Volatility Forecasting**  
  Uses GARCH(1,1) to forecast future volatility step-by-step.

- 🔁 **Live Model Updates**  
  Dynamically refits the model on new data during the simulation.

- 📊 **Interactive Visualization**  
  Built with **Streamlit** and **matplotlib** for easy-to-use UI.

- 📝 **Logging**  
  Forecasted volatility is logged into `logs/forecast.log` with timestamps and forecasted values.

- 💾 **Model Management**  
  Latest trained model can be loaded and reused using `load_model()` function.

---

## 🚧 Future Improvements

- 📉 Compare performance with **ARIMA**, **LSTM**, and **Hybrid models**
- 🧠 Use **Bayesian GARCH** or **EGARCH** for better modeling of asymmetries
- 🧪 Add **backtesting module** for forecast accuracy evaluation (e.g., RMSE, MAE)
- 🌐 Add support for **multiple assets** or **portfolio-level forecasting**
- 🔒 Add **exception handling** and **robust error logging**
- 📦 Package as a **Python module** for easy reuse
- 🐳 **Dockerize** the app for deployment in containerized environments
- ☁️ Deploy to **Streamlit Cloud** or **Heroku**

---

## Author
K.Ajith Varma (ajithk1503)



## 🔧 Installation & Running Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/garch-volatility-forecasting.git
   cd garch-volatility-forecasting
