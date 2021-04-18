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
    choice = st.sidebar.selectbox("choose", options, 1)
    if(choice == options[0]):
        stockLookUp()
    else:
        calculator()

def calculator():
    st.title('Calculator')

    selected_stock = st.text_input("Enter ticker:", "GME").upper()
    share_amount = st.text_input("Enter share amount:", 0)
    startDate = st.date_input("Enter Start Date", max_value = date.today())
    endDate = st.date_input("Enter End Date", min_value = startDate, max_value = (startDate + datetime.timedelta(days=365))) 
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
                    font-size:3vw;
                }
                </style>
                """, unsafe_allow_html=True)

    gain = Stock(selected_stock, startDate=startDate, endDate=endDate)
    calc = gain.calculateCapitalGain(share_amount)
    st.write('<p class="font-size">Capital Gain for ', share_amount, 'shares in ', selected_stock, ':', calc, '</p>', unsafe_allow_html=True)
    # st.text()

    # mainStock = Stock(selected_stock, timePeriod)
    # mainStock.graph()

    

def stockLookUp():
    st.title('Stock App')
    selected_stock = st.text_input("Enter ticker:", "GME").upper()

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