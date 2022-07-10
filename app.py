import streamlit as st
import yfinace as finance

def get_ticker(name):
	company = finance.Ticker(name)
	return company
	
st.title('Stock Market App')
st.header('Stock Market Web site using Streamlit & yahoo finance')
st.sidebar.header('Test') 

company1 = get_ticker('GOOGL')
company2 = get_ticker('MSFT')

google = finance.download('GOOGL', start='2021-10-01', end='2021-10-01')

