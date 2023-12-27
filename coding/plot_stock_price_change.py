# filename: plot_stock_price_change.py
import matplotlib.pyplot as plt
import yfinance as yf

# Get the stock data
nvda = yf.Ticker("NVDA")
tesla = yf.Ticker("TSLA")

# Get the stock prices
nvda_prices = nvda.history(period="ytd")["Close"]
tesla_prices = tesla.history(period="ytd")["Close"]

# Calculate the stock price change
nvda_change = (nvda_prices[-1] - nvda_prices[0]) / nvda_prices[0] * 100
tesla_change = (tesla_prices[-1] - tesla_prices[0]) / tesla_prices[0] * 100

# Plot the stock price change
plt.plot(nvda_prices.index, nvda_change, label="NVDA")
plt.plot(tesla_prices.index, tesla_change, label="TSLA")
plt.xlabel("Date")
plt.ylabel("Stock Price Change (%)")
plt.title("NVDA and TSLA Stock Price Change YTD")
plt.legend()
plt.show()