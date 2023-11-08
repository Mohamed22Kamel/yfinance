import yfinance as yf


def current_price(instrument):
    data = yf.Ticker(instrument).history(period="1m")
    return data.iloc[-1]
