import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import requests

# --- Page title ---
st.set_page_config(page_title="📈 Real-Time Stock Tracker", layout="wide")
st.title("📈 Real-Time Stock Market Dashboard")

# --- Sidebar: Ticker Selection ---
st.sidebar.header("Select a Stock")

popular_tickers = ['AAPL', 'TSLA', 'GOOGL', 'MSFT', 'AMZN', 'NFLX', 'NVDA']
ticker = st.sidebar.selectbox("Choose a stock ticker:", popular_tickers)
custom_ticker = st.sidebar.text_input("Or enter another ticker:")

if custom_ticker:
    ticker = custom_ticker.upper()

# --- Sidebar: Time Range Selection ---
st.sidebar.subheader("📆 Select Time Range")
today = datetime.date.today()

range_option = st.sidebar.selectbox("Choose a period:", ("1M", "3M", "6M", "1Y", "YTD", "MAX"))

if range_option == "1M":
    start_date = today - datetime.timedelta(days=30)
elif range_option == "3M":
    start_date = today - datetime.timedelta(days=90)
elif range_option == "6M":
    start_date = today - datetime.timedelta(days=180)
elif range_option == "1Y":
    start_date = today - datetime.timedelta(days=365)
elif range_option == "YTD":
    start_date = datetime.date(today.year, 1, 1)
elif range_option == "MAX":
    start_date = None

end_date = today

# --- Fetch Stock Data ---
if start_date:
    data = yf.download(ticker, start=start_date, end=end_date)
else:
    data = yf.download(ticker, end=end_date)

# --- Check for empty data ---
if data.empty:
    st.warning("⚠️ No data found for this ticker and date range.")
    st.stop()

# --- Sidebar: Moving Averages ---
st.sidebar.subheader("📐 Moving Averages")

show_sma = st.sidebar.checkbox("Show Simple Moving Average (SMA)")
show_ema = st.sidebar.checkbox("Show Exponential Moving Average (EMA)")

if show_sma:
    sma_period = st.sidebar.slider("SMA Period (days)", min_value=5, max_value=100, value=20)
    data['SMA'] = data['Close'].rolling(window=sma_period).mean()

if show_ema:
    ema_period = st.sidebar.slider("EMA Period (days)", min_value=5, max_value=100, value=20)
    data['EMA'] = data['Close'].ewm(span=ema_period, adjust=False).mean()

# --- Price Chart ---
st.subheader(f"📊 {ticker} Closing Price Chart ({range_option})")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data.index, data['Close'], label='Close Price', color='blue')

if show_sma:
    ax.plot(data.index, data['SMA'], label=f"SMA {sma_period}", color='orange')
if show_ema:
    ax.plot(data.index, data['EMA'], label=f"EMA {ema_period}", color='green')

ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.set_title(f"{ticker} Closing Price Over Time")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# --- Daily Return Chart ---
data['Daily Return (%)'] = data['Close'].pct_change() * 100
data.dropna(inplace=True)

st.subheader("📈 Daily Returns (%)")

fig2, ax2 = plt.subplots(figsize=(10, 3))
ax2.bar(data.index, data['Daily Return (%)'], color='skyblue')
ax2.axhline(0, color='black', linewidth=0.5)
ax2.set_ylabel("Return (%)")
ax2.set_title("Daily Returns Over Time")
ax2.grid(True)

st.pyplot(fig2)

# --- Latest Available Data ---
st.subheader("🔍 Latest Available Data")

styled_row = data.tail(1).style.format({
    "Open": "${:.2f}",
    "Close": "${:.2f}",
    "High": "${:.2f}",
    "Low": "${:.2f}",
    "Volume": "{:,.0f}"
})
st.dataframe(styled_row)

# --- News Headlines using Marketaux API ---
st.subheader("📰 Latest News")

API_KEY = "hQNc8e4ckQPu2fUVCXdE9szEPO6ZEGm3OT9Xv8fw"
news_url = f"https://api.marketaux.com/v1/news/all?symbols={ticker}&filter_entities=true&language=en&api_token={API_KEY}"

try:
    response = requests.get(news_url)
    if response.status_code == 200:
        news_data = response.json()
        news_items = news_data.get('data', [])

        if news_items:
            for article in news_items[:5]:
                st.markdown(f"### [{article['title']}]({article['url']})")
                st.write(f"*{article['published_at']}* - {article['source']['name']}")
                st.markdown("---")
        else:
            st.info("No news found for this ticker.")
    else:
        
        pass
except Exception:
    
    pass

# --- Backup links ---
st.markdown(f"🔗 [Search more on Marketaux →](https://marketaux.com/search?q={ticker})")
st.markdown(f"🔗 [More News on Yahoo Finance →](https://finance.yahoo.com/quote/{ticker})")
