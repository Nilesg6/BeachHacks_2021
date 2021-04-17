import streamlit as st
# from datetime import date
import datetime
from datetime import date
# import wikipedia

import yfinance as yf
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

st.title('Stock App')
selected_stock = st.text_input("Enter ticker:").upper()
# inter = st.text_input("Enter time:").upper()

ticker = yf.Ticker(selected_stock)


def load_data(ticker,interval = 'ytd'):
    # print(interval)
    data = ticker.history(period=interval)
    data.reset_index(inplace=True)
    return data


def plot_raw_data(data):
    d = data
    # fig = 0
    # del fig
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=d['Date'], y=d['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=d['Date'], y=d['Close'], name="stock_close"))
    fig.
    # fig.add_trace(go.Scatter(x=data['Date'], y=data['Volume'], name="Volume"))
    # fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

data_load_state = st.text('Loading data...')
if(selected_stock != ""):
    data = load_data(ticker)
    # print(data)
    # # if(data == None)
    data_load_state.text('Loading data... done!')

    st.write('$', selected_stock)

    # print(data)
    # st.subheader('Raw data')
    # st.write(data.tail())

    # Plot raw data
    plot_raw_data(data)

    if(st.button("1mo") == True):
        inter='1mo'
        data = load_data(ticker, inter)
        plot_raw_data(data)