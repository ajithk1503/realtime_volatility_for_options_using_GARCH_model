from arch import arch_model

def fit_garch_model(returns,p=1,q=1):
    model=arch_model(returns*100,vol='GARCH',p=p,q=q)
    return model.fit(disp="off")

def forecast_volatility(model,horizon=5):
    forecast = model.forecast(horizon=horizon)
    return forecast.variance.values[-1]

def update_garch(data):
    model = arch_model(data * 100, vol='GARCH', p=1, q=1)
    result = model.fit(disp='off')
    return result.conditional_volatility.iloc[-1]

