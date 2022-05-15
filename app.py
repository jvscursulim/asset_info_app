import numpy as np
import streamlit as st
import yfinance as yf

from PIL import Image

with st.container():
    
    image = Image.open("financial_market.jpg")
    st.image(image = image, caption = "Image taken from: https://bankersjournalug.com/explainer-what-are-financial-markets/")
    

st.title("Asset information app")

ticker = st.text_input(label = "Asset ticker: ")

st.header(f"{ticker}")
st.header("Most recent data")
st.write("Source: Yahoo Finance API")

col1, col2 = st.columns(2)

if ticker != "":
        
    data = yf.download(tickers = ticker, period = "5d", progress = False)
    delta = np.round(((data["Adj Close"][-2]-data["Adj Close"][-1])/data["Adj Close"][-2])*100, 2)
    
    with col1:
            
        st.metric(label = "Close", value = f"${np.round(data['Adj Close'][-1], 2)}", delta = f"{delta}%")
        st.metric(label = "Transactions volume", value = f"${data['Volume'][-1]}")
        
    with col2:
        
        st.metric(label = "Open", value = f"${np.round(data['Open'][-1], 2)}")
        st.metric(label = "Low", value = f"${np.round(data['Low'][-1], 2)}")
        st.metric(label = "High", value = f"${np.round(data['High'][-1], 2)}")
        
else:
    
    with col1:
                
        st.metric(label = "Close", value = "$0.00", delta = "0.00%")
        st.metric(label = "Transactions volume", value = "0")
    
    with col2:
        
        st.metric(label = "Open", value = "$0.00")
        st.metric(label = "Low", value = "$0.00")
        st.metric(label = "High", value = "$0.00")
    
st.header("Charts and Tables")
time_period = st.selectbox(label = "Select a time period: ", options = ["-","1d", "5d", "1mo", "3mo", "6mo", "1y", "5y", "10y", "ytd", "max"])

if time_period != "-":
        
    data = yf.download(tickers = ticker, period = time_period, progress = False)

    if st.button("Data table"):
            
        st.dataframe(data = data)
            
    if st.button("Close price chart"):
            
        st.write(f"""{ticker} close price in {time_period} ($USD)""")
        st.line_chart(data = data['Adj Close'])

    if st.button("Transaction volume chart"):
            
        st.write(f"""{ticker} transaction volume in {time_period}""")
        st.bar_chart(data = data['Volume'])
    
    
