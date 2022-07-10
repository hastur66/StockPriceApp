import streamlit as st
import yfinance as finance

def get_ticker(name):
	company = finance.Ticker(name)
	return company
	
st.title('Stock Market App')
st.header('Stock Market Web site using Streamlit & yahoo finance')
st.sidebar.header('Demo') 

company1 = get_ticker('GOOGL')
company2 = get_ticker('MSFT')

data1 = company1.history(period='3mo')
data2 = company2.history(period='3mo')

google = finance.download('GOOGL', start='2021-10-01', end='2021-10-01')
microsoft = finance.download('MSFT', start='2021-10-01', end='2021-10-01')

st.write('Google')
st.write(company1.info['longBusinessSummary'])
st.write(google)

st.line_chart(data1.values)

st.write('Microsoft')
st.write(company2.info['longBusinessSummary'])
st.write(microsoft)

st.line_chart(data2.values)
