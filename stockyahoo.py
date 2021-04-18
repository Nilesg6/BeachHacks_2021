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
class Trade():

    def __init__(self, wallet = 1000):
        self.wallet = wallet
        self.portfolio = {}
        self.stockData = []
        self.worth = 0
        self.initial = wallet

    def buy(self, tickers, date, shares):
        # buyStock = Stock(ticker)
        # print(date)
        # data = buyStock.load_data_range(startDate= date - datetime.timedelta(days=1), endDate= date)
        data = yf.download(tickers, start = date)
        # self.stockData = data
        print(data)
        if(len(data['Close']) > 0):
            purchase = 0
            for i, j in zip(tickers, shares):
                purchase += float(data['Close'][i][0]) * float(j)
            print(" pur", purchase)
            # purchase = sharePrice * float(shares
            if self.confirmBuy(purchase):
                self.updatePortfolio(tickers, shares)
                self.wallet -= round(purchase, 2)
                self.worth += round(purchase, 2)
                print(" por", self.portfolio)
                print(" wal", self.wallet)
                print(" wor", self.worth)
                st.subheader("Purchase Complete!")
                st.write("Wallet =", self.wallet)
                st.write("Portfolio Worth =", self.worth)
                return self.portfolio
            st.write("Insufficient Funds")

        
    def sell(self, tickers, date, shares):
        print(" tic", tickers)
        # if len(tickers) == 0:
        #     st.write("Inadequate Information")
        #     return
        data = yf.download(tickers, end = date)
        # self.stockData = data
        # self.worth = self.getPortfolioWorth()
        print(self.stockData)
        # print(" wal", self.wallet)
        print(" wor", self.worth)
        print(" por", self.portfolio)

        if(len(data['Close']) > 0):
            sellPrice = 0
            for i, j in zip(tickers, shares):
                sellPrice += float(data['Close'][i][len(data['Close']) - 1]) * float(j)
            print(" sel", sellPrice)
            if self.confirmSell(sellPrice):
                # self.updatePortfolio(tickers, shares)
                self.wallet += round(sellPrice, 2)
                self.worth =  round(self.wallet - float(self.initial), 2)
                print(" wal", self.wallet)
                print(" wer", self.worth)
                print(self.portfolio)
                st.subheader("Trade Complete!")
                st.write("Wallet =", round(self.wallet, 2))
                st.write("Capital Gain =", self.worth)


        # data = yf.download(ticker, start = date)
        # if(len(data['Close']) > 0):
        #     sharePrice = data['Close'][0]
        #     sold = sharePrice * shares
        #     if self.confirmSell(ticker, shares):
        #         self.updatePortfolio(ticker, -1*shares)
        #         self.wallet += sold
        
    def confirmBuy(self, purchase):
        if self.wallet >= purchase:  #purchase = shares * price > 0
            return True
        return False
         
    def confirmSell(self, sellPrice):
        if(self.worth >= sellPrice):
           return True	
        return False

    def updatePortfolio(self, tickers, shares):
        # if(ticker not in self.portfolio.keys()):
        #     self.portfolio[ticker] = 0
        for i, j in zip(tickers, shares):
            self.portfolio[i] = int(j)
        # print(self.portfolio)
        # return list(self.portfolio.keys())

    # def getPortfolioWorth(self):
    #     for i, j in self.portfolio.items():
    #         self.worth += self.stockData['Close'][i][len(self.stockData['Close']) - 1] * float(j)
    #         print(" sum", self.worth)
    #     return round(self.worth, 2)

    def getWallet(self):
        return self.wallet

    def graph(self):
        #, date_col = stockData['Date'], open_col = stockData['Open']):
        # args = [date_col, open_col]
        # g = 0
        # del g
        g = Graph()
        g.plot_raw_data(self.stockData)

class Stock():

    tickerString = ""
    ticker = ""
    stockData = []
    period = ""
    startDate = 0
    endDate = 0

    def __init__(self, selected_stock, period = '1y', startDate = 0, endDate = 0):
        self.ticker = yf.Ticker(selected_stock)
        self.tickerString = selected_stock
        self.period = period
        self.stockData = self.load_data(self.period )
        self.startDate = startDate
        self.endDate = endDate
        

    def load_data(self, period, interval = '1d'):
        if(period == '1d'):
            interval = '15m'
        data = self.ticker.history(period, interval)
        # print(data[0])
        # data = ticker.history("1d", "1m")
        data.reset_index(inplace=True)
        return data

    def load_data_range(self, startDate, endDate):
        # if(startDate == endDate):
        #     data = yf.download(, start = startDate, end = endDate, interval='15m')
        # else:
        if(self.tickerString!= ""):
            inter = '1d'
            if((endDate - startDate).days <= 3):
                inter = '15m'
                data = self.ticker.history(period='1d', interval = inter, start=startDate, end=endDate)
            else:
                data = yf.download(self.tickerString, start = startDate, end = endDate, interval = inter)
            self.stockData = data
        # print(data[0])
        # data = ticker.history("1d", "1m")
            data.reset_index(inplace=True)
            return data
        
    def calculateCapitalGain(self,shares): # startDate, endDate):
        # startData = self.load_data_range(self.startDate, self.startDate)
        # endData = self.load_data_range(self.endDate, self.endDate)
        # if(self.stockData != )
        # if()
        rangeData = self.load_data_range(self.startDate, self.endDate)
        print(rangeData)
        # print( "RANGE" , rangeData['Date'])
        if(len(rangeData['Open']) > 1):
            startPrice = rangeData['Open'][0]
            endPrice = rangeData['Close'][len(rangeData['Close']) - 1]
            print(startPrice , endPrice)
            total = round(float(shares) * (endPrice - startPrice), 2)
            return total

    def getStockData(self):
        return self.stockData

    def graph(self):
        #, date_col = stockData['Date'], open_col = stockData['Open']):
        # args = [date_col, open_col]
        # g = 0
        # del g
        g = Graph()
        g.plot_raw_data(self.stockData)

    def background(self):
        return(self.ticker.info['longBusinessSummary'])


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


