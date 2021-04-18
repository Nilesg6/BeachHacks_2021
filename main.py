import streamlit as st
# from datetime import date
import datetime
from datetime import date
# import wikipedia
import yfinance as yf
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from stockyahoo import Stock



st.title('Stock App')
selected_stock = st.text_input("Enter ticker:").upper()

time = ["1d", "5d", "1mo", "ytd", "1y"]


timePeriod = st.selectbox("Choose a demo", time, 4)
print(timePeriod)

mainStock = Stock(selected_stock, timePeriod)
sD = mainStock.getStockData()

mainStock.graph()

# if(sD != []):
# print(sD)


# inter = st.text_input("Enter time:").upper()

# ticker = yf.Ticker(selected_stock)

# data_load_state = st.text('Loading data...')
# if(selected_stock != ""):
#     data = stockyahoo.load_data(ticker)
#     # print(data)
#     # # if(data == None)
#     data_load_state.text('Loading data... done!')

#     st.write('$', selected_stock)

#     # print(data)
#     # st.subheader('Raw data')
#     # st.write(data.tail())

#     # Plot raw data
#     stockyahoo.plot_raw_data(data)

#     if(st.button("1mo") == True):
#         inter='1mo'
#         data = stockyahoo.load_data(ticker, inter)
#         stockyahoo.plot_raw_data(data)