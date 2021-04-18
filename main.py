import streamlit as st
# from datetime import date
import datetime
from datetime import date
# import wikipedia
import yfinance as yf
import pandas as pd
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly
from plotly import graph_objs as go
from stockyahoo import Stock
from stockyahoo import Trade

def run():
    options = ["Stock Look Up", "Calculator", "Paper Trade"]
    choice = st.sidebar.selectbox("choose", options, 2)
    if choice == options[0]:
        stockLookUp()
    if choice == options[1]:
        calculator()
    if choice == options[2]:
        paperTrade()

def paperTrade():
    st.title('Paper Trade')

    # wallet = 0
    wallet = st.text_input("Enter wallet amount ($):", 1000)
    investments = Trade(wallet)

    selected_stock = st.text_input("Enter ticker:", "GME").upper()
    
    lookupDate = st.date_input("Enter Buy Date", value = date.today(), max_value = date.today())

    
    investments.buy(selected_stock, lookupDate, 5)
    investments.sell(selected_stock, lookupDate + datetime.timedelta(days=1), 5)
    st.write(investments.getWallet())

    # portfolio = [['2020-09-01', 'GME', 1000], ['2021-04-01', 'GME', 100]]
    # portfolio.append(['XXXX-XX-XX', 'GME', 10])

    
    # lookupDate = st.date_input("Enter Sell Date", value = date.today(), max_value = date.today())
    
    # # if st.button("Open") == True:
    # #     price = dummy_stock.getOpenPrice()
    # # elif st.button("Close") == True:


    # dummy_stock = Stock(selected_stock, endDate=lookupDate)
    # stock1 = Stock(selected_stock, endDate=lookupDate)
    # stock2 = Stock(selected_stock, endDate=lookupDate)

    # price = dummy_stock.getClosePrice()
    # stage = price * shares

    # trader = Trade()

    # if stage <= wallet:
    #     portfolio.add(trader.buy(stock1))
    #     portfolio.remove(trader.sell(stock1))


    # st.header("Portfolio")

    # st.dataframe(pd.DataFrame(portfolio, columns={
    #     "date": portfolio[:0],
    #     "ticker": portfolio[:1],
    #     "shares": portfolio[:2]
    # }))


def calculator():
    st.title('Calculator')

    selected_stock = st.text_input("Enter ticker:", "GME").upper()
    share_amount = st.text_input("Enter share amount:", 1)
    startDate = st.date_input("Enter Start Date", value = date.today() - datetime.timedelta(days=1), max_value = date.today() - datetime.timedelta(days=1))
    limit = startDate + datetime.timedelta(days=365)
    if limit >= date.today():
        limit = date.today()
    endDate = st.date_input("Enter End Date", value = date.today(), min_value = startDate, max_value = limit) 
    # if (endDate - startDate).days <= 365:
        # mainStock = Stock(selected_stock, start_date=startDate, end_date=endDate)
        # mainStock.calculateCapitalGain()
        # mainStock.graph()

    # time = ["1d", "5d", "1mo", "ytd", "1y"]
    # timePeriod = st.selectbox("Choose a demo", time, 4)

    # debug
    # print(timePeriod)
    # diff = (endDate - startDate).days
    # d = st.text_area('Capital Gain', value=diff)

    st.markdown("""
                <style>
                .font-size {
                    font-size:2vw;
                }
                </style>
                """, unsafe_allow_html=True)

    # NOTE: print out start and end price
    gain = Stock(selected_stock, startDate=startDate, endDate=endDate)
    calc = gain.calculateCapitalGain(share_amount)
    st.write('<p class="font-size">Capital Gain for ', share_amount, 'shares in ', selected_stock, ': $', str(calc), '</p>', unsafe_allow_html=True)
    gain.graph()
    # st.text()

    # mainStock = Stock(selected_stock, timePeriod)
    # mainStock.graph()

    

def stockLookUp():
    st.title('Stock App')
    selected_stock = st.text_input("Enter ticker:", "GME").upper()

    time = ["1d", "5d", "1mo", "ytd", "1y"]


    timePeriod = st.selectbox("Choose time period", time, 4)
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