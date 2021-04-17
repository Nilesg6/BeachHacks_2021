import streamlit as st
# from datetime import date
import datetime
from datetime import date
# import wikipedia

import yfinance as yf
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

# st.title('Stock App')
# selected_stock = st.text_input("Enter ticker:").upper()
# # inter = st.text_input("Enter time:").upper()

# ticker = yf.Ticker(selected_stock)

#sy
#ticker
#data

#seperate
#graph
    #period
    #ticker
    #axes
    #header
    #

class Stock():

    ticker = []
    stockData = []

    def __init__(self, selected_stock):
        ticker = yf.Ticker(selected_stock)
        self.stockData = self.load_data(ticker)

    def load_data(self, ticker,interval = 'ytd'):
        # print(interval)
        data = ticker.history(period=interval)
        data.reset_index(inplace=True)
        return data
        
    def getStockData(self):
        return self.stockData

# class Graph():
    
#     def 

    # def plot_raw_data(data):
    #     d = data
    #     # fig = 0
    #     # del fig
    #     fig = go.Figure()
    #     #scatter object class has list of all traces
    #     fig.add_trace(go.Scatter(x=d['Date'], y=d['Open'], name="stock_open"))
    #     fig.add_trace(go.Scatter(x=d['Date'], y=d['Close'], name="stock_close"))
    #     fig.del()
    #     # fig.add_trace(go.Scatter(x=data['Date'], y=data['Volume'], name="Volume"))
    #     # fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    #     st.plotly_chart(fig)

# data_load_state = st.text('Loading data...')
# if(selected_stock != ""):
#     data = load_data(ticker)
#     # print(data)
#     # # if(data == None)
#     data_load_state.text('Loading data... done!')

#     st.write('$', selected_stock)

#     # print(data)
#     # st.subheader('Raw data')
#     # st.write(data.tail())

#     # Plot raw data
#     plot_raw_data(data)

#     if(st.button("1mo") == True):
#         inter='1mo'
#         data = load_data(ticker, inter)
#         plot_raw_data(data)