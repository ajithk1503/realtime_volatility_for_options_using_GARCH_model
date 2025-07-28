import pandas as pd

def load_returns(path='data/processed/NIFTY_500_with_garch_volatility.csv'):
    df = pd.read_csv(path)
    return df['log_return']

