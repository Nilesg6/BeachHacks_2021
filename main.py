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

def run():
    options = ["Stock Look Up", "Calculator"]
    choice = st.sidebar.selectbox("choose", options)
    if(choice == options[0]):
        stockLookUp()
    else:
        calculator()

def calculator():
    startDate = st.date_input("Enter Start Date", min_value = (datetime.datetime.now() - datetime.timedelta(days=1*365)), max_value = date.today())
    endDate = st.date_input("Enter End Date", min_value = (datetime.datetime.now() - datetime.timedelta(days=1*365)), max_value = date.today()) 

    

def stockLookUp():
    st.title('Stock App')
    selected_stock = st.text_input("Enter ticker:").upper()

    time = ["1d", "5d", "1mo", "ytd", "1y"]


    timePeriod = st.selectbox("Choose a demo", time, 4)
    print(timePeriod)

    mainStock = Stock(selected_stock, timePeriod)
    sD = mainStock.getStockData()

    mainStock.graph()


run()

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