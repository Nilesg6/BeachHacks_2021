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


class Stock():

    ticker = []
    stockData = []
    period = ""

    def __init__(self, selected_stock, period):
        self.ticker = yf.Ticker(selected_stock)
        self.period = period
        self.stockData = self.load_data(self.ticker, self.period )
        

    def load_data(self, ticker, period, interval = '1d'):
        if(period == '1d'):
            interval = '15m'
        data = ticker.history(period, interval)
        # print(data[0])
        # data = ticker.history("1d", "1m")
        data.reset_index(inplace=True)
        return data
        
    def getStockData(self):
        return self.stockData

    def graph(self):
        #, date_col = stockData['Date'], open_col = stockData['Open']):
        # args = [date_col, open_col]
        # g = 0
        # del g
        g = Graph()
        g.plot_raw_data(self.stockData)


#seperate
#graph
    #period
    #ticker
    #axes
    #header
    #
class Graph():

    figure_bettername = go.Figure()
    
    def __init__(self): #, args):
        self.figure_bettername = go.Figure()
        self.chartplot = st.empty()
        # self.period = args[0]
        # self.ticker = args[1]
        # self.axes = args[2]
        # self.header = args[3]

    def plot_raw_data(self, data):
        d = data
        xVar = 'Date'
        if('Datetime' in d):
            xVar = 'Datetime'
        # fig = 0
        # del fig
        #scatter object class has list of all traces
        # self.figure_bettername = go.Figure(go.Ohlc(x=d['Datetime'], open=d['Open'], high=d['High'], low=d['Low'], close=d['Close']))
        
        self.figure_bettername = go.Figure(go.Ohlc(x=d[xVar], open=d['Open'], high=d['High'], low=d['Low'], close=d['Close']))
       
        # self.figure_bettername.add_trace()
        # self.figure_bettername.add_trace(go.Scatter(x=d['Date'], y=d['High'], name="stock_high"))
        # self.figure_bettername.add_trace(go.Scatter(x=d['Date'], y=d['Low'], name="stock_low"))
        # self.figure_bettername.update_xaxes(rangeslider_range=d['Date'])
        # fig.del()
        # fig.add_trace(go.Scatter(x=data['Date'], y=data['Volume'], name="Volume"))
        # fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)

        self.chartplot.empty()
        self.chartplot = st.plotly_chart(self.figure_bettername)

    

    # def update_fig(self, data):
    #     d = data
    #     self.figure_bettername.update_traces(overwrite=True)

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