import streamlit as st
# from datetime import date
import datetime
from datetime import date
import yfinance as yf
import pandas as pd
from plotly import graph_objs as go
from stockyahoo import Stock
from stockyahoo import Trade

help_ticker = "Enter the ticker value for a company of your choice. A Google search may help with this."
help_share = "Enter the amount of shares you want to \"purchase\". Shares represent fractional ownership of the company selected."
help_wallet = "Enter the amount of money in US dollars you want to practice trading with. This fictional money is the start of paper trading"
help_stockamount = "Enter the amount of stocks you want to \"purchase\"."
help_date_start = "Select the date you want to start tracking or \"buying\" at."
help_date_end = "Select the date you want to end tracking or \"selling\" at."
help_time = "Select the time period which you want track or \"hold\" for."
help_side = "Select the page you want to practice in."
help_graph = "The OHLC graph displays the high and low price of stock in a period of time. Each line represents the statistics for each 15 minutes for 1 day tracking or individual day in the period of time."

def run():
    options = ["Home","Stock Look Up", "Calculator", "Paper Trade"]
    choice = st.sidebar.selectbox("Choose Page", options, 0, help=help_side)
    if choice == options[0]:
        home()
    if choice == options[1]:
        stockLookUp()
    if choice == options[2]:
        calculator()
    if choice == options[3]:
        paperTrade()

def paperTrade():
    st.title('Paper Trade')

    # wallet = 0
    wallet = int(st.text_input("Enter wallet amount ($):", 1000, help=help_wallet))
    investments = Trade(wallet=wallet)
    stock_amount = int(st.text_input("Enter amount of stocks:", 2, help=help_stockamount))
    portfolio = {}
    while stock_amount:
        stock_amount-=1
        select_stock = st.text_input("Enter ticker:", key=stock_amount, help=help_ticker).upper()
        share_amount = st.text_input("Enter share amount:", key=stock_amount, help=help_share)
        portfolio[select_stock] = share_amount
        # stock_list = investments.updatePortfolio(st.text_input("Enter ticker:", key=stock_amount).upper(), 2)
    
    beginTrade = st.date_input("Enter Buy Date", value = date.today() - datetime.timedelta(days=1), max_value = date.today() - datetime.timedelta(days=1), help=help_date_start)
    # Repetitive Code
    limit = beginTrade + datetime.timedelta(days=365)
    if limit >= date.today():
        limit = date.today()
    endTrade = st.date_input("Enter Sell Date", value = date.today(), min_value = beginTrade + datetime.timedelta(days=1), max_value = limit, help=help_date_end)
    
    tempPortfolio = {}
    if st.button("Activate") == True:
        tempPortfolio = investments.buy(list(portfolio.keys()), beginTrade, list(portfolio.values()))
        if tempPortfolio is None:
            st.write("Inadequate Information")
            st.write("Try a different date")
            return
        investments.sell(list(tempPortfolio.keys()), endTrade, list(tempPortfolio.values()))
        # investments.graph()

    
    # investments.buy(selected_stock, lookupDate, 5)
    # investments.sell(selected_stock, lookupDate + datetime.timedelta(days=1), 5)
    # st.write(investments.getWallet())

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

    selected_stock = st.text_input("Enter ticker:", "GME", help=help_ticker).upper()
    share_amount = st.text_input("Enter share amount:", 1, help=help_share)
    startDate = st.date_input("Enter Start Date", value = date.today() - datetime.timedelta(days=1), max_value = date.today() - datetime.timedelta(days=1), help=help_date_start)
    limit = startDate + datetime.timedelta(days=365)
    if limit >= date.today():
        limit = date.today()
    endDate = st.date_input("Enter End Date", value = date.today(), min_value = startDate + datetime.timedelta(days=1), max_value = limit, help=help_date_end) 
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
    selected_stock = st.text_input("Enter ticker:", "GME", help=help_ticker).upper()

    time = ["1d", "5d", "1mo", "ytd", "1y"]


    timePeriod = st.selectbox("Choose time period", time, 4, help=help_time)
    print(timePeriod)

    mainStock = Stock(selected_stock, timePeriod)
    # sD = mainStock.getStockData()

    st.subheader("OHLC Graph:\nThe OHLC graph displays the high, low, closing, and opening prices of a stock in a period of time. Each line represents the statistics for each 15 minutes for 1 day tracking or individual day in the period of time.")
    mainStock.graph()
    st.subheader("Background Info")
    mainStock.background()  
    st.write(mainStock.background())


def home():
    st.subheader("Welcome")
    st.write("With the recent developments over the past year, the stock market has been making headlines quite frequently. It can be easy to dismiss the stock market as dangerous and requiring plenty of prior knowledge. While there may be some truth to that, it doesn't have to be so foriegn.")

    st.subheader("Our Goal")
    st.write("We have created tools to help individuals who are new to the stock market and would love to learn more. All while taking none of the finanical risk.") 
    st.write("The Stock Look Up allows you to see the past year of a company's trading history. Taking a closer look at the graph will show the daily open, close, high, and low.")
    st.write("The calculator allows you to visualize the market growth of a company over a time period. And with using real numbers, we can estimate how many shares would have changed in value.")
    st.write("Paper Trade allows you to simulate holding a portfolio of mulitiple different companies. You can choose how many stocks and how many shares you wish to purchase based off your wallet. Then after choosing a buy and sell date you can see how your portfolio preformed.")


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