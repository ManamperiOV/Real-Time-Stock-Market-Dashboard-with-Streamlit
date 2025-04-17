# Real-Time-Stock-Market-Dashboard-with-Streamlit

An interactive stock analysis tool built using **Python**, **Streamlit**, and **yFinance** to visualize real-time financial data.

## 🔧 Features

- **📊 Live Price Chart** – Pulls real-time data from Yahoo Finance and displays stock performance for selectable time ranges (1M, 3M, 6M, 1Y, YTD, MAX).
- **📐 Moving Averages** – Optionally display Simple Moving Average (SMA) and Exponential Moving Average (EMA), customizable by the number of days.
- **📈 Daily Returns Chart** – Calculates and visualizes the percentage change in stock price from day to day.
- **🔍 Latest Market Stats** – Shows the most recent open, close, high, low, and volume data for the selected stock.
- **📰 Financial News Feed** – Integrates with the [Marketaux API](https://marketaux.com/) to display the latest news headlines related to the selected stock.
- **🔗 Backup Links** – Direct links to Marketaux and Yahoo Finance for further stock analysis.
- **🎛️ Interactive Interface** – Built entirely with **Streamlit**, no need to refresh the app when switching stocks or toggling features.

## 📦 Tech Stack

- Python
- Streamlit
- yFinance
- Pandas
- Matplotlib
- Marketaux News API

## 🧠 Skills Demonstrated

- API integration and error handling
- Financial data processing and analysis
- Time series visualization
- Interactive dashboard development
- Clean UI with data filtering and conditional displays

## 📁 Dataset Source

Stock data is fetched live from Yahoo Finance via the `yfinance` Python library.

## 🚀 Getting Started

```bash
streamlit run dashboard.py

![Screenshot (46)](https://github.com/user-attachments/assets/1b66a26d-cfd4-47f8-90bf-02b424e4ff67)
![Screenshot (47)](https://github.com/user-attachments/assets/18901ede-def9-4a32-ba87-4c302bc2375c)
