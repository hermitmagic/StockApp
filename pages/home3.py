
#import streamlit as st
#from datetime import date
    
#import numpy as np
#from PIL import  Image
    
   # from mplfinance.original_flavor import candlestick_ohlc
    #import matplotlib.dates as mdates
    #from PIL import Image
   # import pandas as pd
    #import pandas_datareader.data as web
    #import numpy as np
    #import matplotlib.pyplot as plt
    #import seaborn as sns

    
#import yfinance as yf
#from prophet import Prophet
#from prophet.plot import plot_plotly
#from plotly import graph_objs as go
import streamlit as st
from datetime import date
import datetime
import pandas as pd   
import numpy as np
from PIL import  Image
import yfinance as yf

import plotly.express as px
from plotly import graph_objs as go
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
    #BackGround
    
def app():
    try:
        START = "2017-01-01"
        TODAY=(date.today()+ datetime.timedelta(days=1)).strftime("%Y-%m-%d") 

        

        


       # stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
        #selected_stock = st.selectbox('Select dataset for prediction', stocks)
        selected_stock = st.text_input("Enter the Stock Code of company","AAPL")
        btn= st.button('Enter')

        if btn:
            ticker = yf.Ticker(selected_stock)
            inf = ticker.info
            df1 = pd.DataFrame().from_dict(inf, orient="index").T
            df1[['logo_url', 'shortName', 'longBusinessSummary']]
        
            st.subheader(df1['shortName'].values[0])
        
            st.write(df1['longBusinessSummary'].values[0])

            
            def load_data(ticker):
                
                data = yf.download(ticker, START, TODAY)
                data.reset_index(inplace=True)
                

                return data

            #data_load_state = st.text('Loading data...')
            data = load_data(selected_stock)
            #data_load_state.text('Loading data... done!')
            
            st.subheader('Opening vs Closing price')
            #st.write(data.tail())

            # Plot raw data
            def plot_raw_data():
                
        	    fig = go.Figure()
        	    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
        	    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
        	    fig.layout.update( xaxis_rangeslider_visible=True)
        	    fig.update_layout(width=900,height=600)
        	    st.plotly_chart(fig)
            plot_raw_data()
            
            #  Moving Average
            
            st.subheader('Moving Average')
            def moving_average():


                data["mov_avg_close"] = data['Close'].rolling(window=int(50),min_periods=0).mean()
                st.write('1. Plot of Stock Closing Value ')
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=data['Date'], y=data['mov_avg_close'], name="mov_avg_close"))
                fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
                fig.layout.update( xaxis_rangeslider_visible=True)
                fig.update_layout(width=900,height=600)
                st.plotly_chart(fig)
                #st.line_chart(data[["mov_avg_close","Close"]])
                data["mov_avg_open"] = data['Open'].rolling(window=int("50"),min_periods=0).mean()
               
                st.write('2. Plot of Stock Open Value  ')     
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=data['Date'], y=data['mov_avg_open'], name="mov_avg_open"))
                fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
                fig.layout.update( xaxis_rangeslider_visible=True)
                fig.update_layout(width=900,height=650)
                st.plotly_chart(fig)
                
                #st.line_chart(data[["mov_avg_open","Open"]])
            moving_average()
            
            # Candle-Stick Graph
            
            st.subheader('Candle Stick Graph')
            #days= st.text_input("Enter number of days for  for OHLC CandleStick Chart", "50")
            
            def candle_stick(stock):
                # command is calling Yahoo Finance API for the specified stock 
                #for a period of 1 day and at an interval of 1 minute
                st.write("Candlesticks are useful when trading as they show four price points (open, close, high, and low) throughout the period of time the trader specifies.")
                st.write(" When the real body is filled in red , it means the close was lower than the open. If the real body is green, it means the close was higher than the open.")
                
                
                df = yf.download(tickers=selected_stock,period='1d',interval='1m')
            # Declare plotly figure (go)
                fig=go.Figure()
            
                fig.add_trace(go.Candlestick(x=df.index,open=df['Open'],high=df['High'],low=df['Low'],close=df['Close'], name = 'market data'))

                fig.update_layout(
                    title= str(stock)+' Live Share Price:',
                    yaxis_title='Stock Price ')               

                fig.update_xaxes(
                    rangeslider_visible=True,
                    rangeselector=dict(
                        buttons=list([
                            dict(count=15, label="15m", step="minute", stepmode="backward"),
                            dict(count=45, label="45m", step="minute", stepmode="backward"),
                            dict(count=1, label="HTD", step="hour", stepmode="todate"),
                            dict(count=3, label="3h", step="hour", stepmode="backward"),
                            dict(step="all")
                            ])
                        )
                    )  
                fig.update_layout(width=900,height=650)
                st.plotly_chart(fig)

                

            candle_stick(selected_stock)
                
            

            #n_years = st.slider('Years of prediction:', 1, 4)
            period = 3 * 365
                 # Predict forecast with Prophet.
            df_train = data[['Date','Close']]
            df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

            #m = Prophet()
            #m.fit(df_train)
            #future = m.make_future_dataframe(periods=period)
            #forecast = m.predict(future)

            # Show and plot forecast
            #st.subheader('Forecast data')
            #st.write(forecast.tail())
            
            #st.write(f'Forecast plot for 3 years')
            #fig1 = plot_plotly(m, forecast)
            #st.plotly_chart(fig1)
            
            #st.write("Forecast components")
            #fig2 = m.plot_components(forecast)
            #st.write(fig2)
            
            #metric_df = forecast.set_index('ds')[['yhat']].join(df_train.set_index('ds').y).reset_index()
            #metric_df.dropna(inplace=True)
            #r2=r2_score(metric_df.y, metric_df.yhat)
            #st.write('R2 Score : ',r2)
        
    except:
        st.subheader('Please write the legitimate Code')
        pass
        

        
        


    
        
            
            

        

       
    


   