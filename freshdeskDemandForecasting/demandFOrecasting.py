import json
import datetime
import pandas as pd
import numpy as np
import sys
import matplotlib.pylab as plt
import matplotlib.pyplot as mplt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] =15,6
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima_model import ARIMA


#Reading data and converting in to time series and aggregating in to 15 minute interval
def read_data(inputFile):
	df = pd.read_json(inputFile)
	df['time'] = pd.to_datetime(df['time'])
	df.set_index('time', inplace = True)
	df['count'] = 1
	agg_df = df.resample('15T',how='sum')

	#Replacing missing values by 0. So if count is missing that means for that 15 minutes there are no requests.
	agg_df[agg_df['count'].isnull()] = 1


	size = int(len(agg_df) * 0.66)
	train, test = agg_df[0:size], agg_df[size:len(agg_df)]
	return train, test

def dataVisualization(agg_df):
	#Showing data
	plt.plot(agg_df, color='blue',label='Original')
	plt.title('Data Visualization through line chart')
	plt.show()

	#box plot
	color = dict(boxes='DarkGreen', whiskers='DarkOrange',medians='DarkBlue', caps='Gray')
	agg_df.plot.box(color=color, sym='r+', label='Visualization of variability of requests.')
	plt.title('Data Visualization through box plot')
	plt.show()



def test_stationarity(agg_df):

	#Visualizing the data
	rolmean = pd.rolling_mean(agg_df, window=24)
	rolstd = pd.rolling_std(agg_df, window=24)

	#Plot rolling statistics:
	orig = plt.plot(agg_df, color='blue',label='Original')
	mean = plt.plot(rolmean, color='red', label='Rolling Mean')
	std = plt.plot(rolstd, color='black', label = 'Rolling Std')
	plt.legend(loc='best')
	plt.title('Rolling Mean & Standard Deviation')
	plt.show()


	'''
	#Perform Dickey-Fuller test:
	print 'Results of Dickey-Fuller Test:'
	dftest = adfuller(agg_df, autolag='AIC')
	print dftest
	dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
	for key,value in dftest[4].items():
		dfoutput['Critical Value (%s)'%key] = value
	print dfoutput
	'''



def differencing(agg_df):
	#Differencing
	ts_log = np.log(agg_df) #TRYING TO REMOVE TREND BY TRANSFORMATION. TAKING LOG OR SQUR ROOT OR CUBE ROOT OF SERIES.
	ts_log_diff = ts_log - ts_log.shift(periods=1)  # shifting by 1 value.
	plt.title("Differencing")
	plt.plot(ts_log_diff)
	ts_log_diff.dropna(inplace=True)
	return ts_log_diff



def ACF_PACF(ts_log_diff):
	#ACF PACF
	lag_acf = acf(ts_log_diff, nlags=60)
	lag_pacf = pacf(ts_log_diff, nlags=20, method='ols')

	#Plot ACF
	plt.subplot(121)
	plt.plot(lag_acf)
	plt.axhline(y=0,linestyle='--',color='gray')
	plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
	plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
	plt.title('Autocorrelation Function')

	#Plot PACF
	plt.subplot(122)
	plt.plot(lag_pacf)
	plt.axhline(y=0,linestyle='--',color='gray')
	plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
	plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
	plt.title('Partial Autocorrelation Function')
	plt.tight_layout()
	plt.show()




def decomposition( agg_df):
	ts_log = np.log(agg_df)
	decomposition = seasonal_decompose(ts_log)
	trend = decomposition.trend
	seasonal = decomposition.seasonal
	residual = decomposition.resid

	#trend, seasonality are separated out from data and we can model the residuals.

	plt.subplot(411)
	plt.plot(ts_log, label='Original')
	plt.legend(loc='best')
	plt.subplot(412)
	plt.plot(trend, label='Trend')
	plt.legend(loc='best')
	plt.subplot(413)
	plt.plot(seasonal,label='Seasonality')
	plt.legend(loc='best')
	plt.subplot(414)
	plt.plot(residual, label='Residuals')
	plt.legend(loc='best')
	plt.tight_layout()
	plt.show()

	#Lets return the residuals to check statiionary of residual.
	ts_log_decompose = residual
	ts_log_decompose.dropna(inplace=True)
	return ts_log_decompose


'''
def ARIMA_model(agg_df, ts_log_diff):
	ts_log = np.log(agg_df)
	model = ARIMA(ts_log, order=(1,1,3))
	result_ARIMA = model.fit(disp=-1)
	plt.plot(ts_log_diff, color='green')
	plt.show()
	plt.plot(result_ARIMA.fittedvalues, color='red')
	#plt.title('RSS: %.4f'% sum((result_ARIMA.fittedvalues-ts_log_diff)**2))
	plt.show()

	#Storing results of ARIMA model.
	predictions_ARIMA_diff = pd.Series(result_ARIMA.fittedvalues, copy=True)
	print predictions_ARIMA_diff.head()
	predictions_ARIMA_diff_cumsum = predictions_ARIMA_diff.cumsum()
	print predictions_ARIMA_diff_cumsum.head()
	predictions_ARIMA_log = pd.Series(ts_log.ix[0], index=ts_log.index)
	predictions_ARIMA_log = predictions_ARIMA_log.add(predictions_ARIMA_diff_cumsum,fill_value=0)
	predictions_ARIMA_log.head()
	predictions_ARIMA = np.exp(predictions_ARIMA_log)
	plt.plot(agg_df, color='green')
	plt.show()
	plt.plot(predictions_ARIMA, color='black')
	#plt.title('RMSE: %.4f'% np.sqrt(sum((predictions_ARIMA-agg_df)**2)/len(agg_df)))
	plt.show()
	return predictions_ARIMA
'''

def ARIMA_model(agg_df,test):
	model = ARIMA(agg_df, order=(4,0,2))
	result_ARIMA = model.fit(disp=0)
	#plt.plot(result_ARIMA.fittedvalues, color='red')
	#plt.title('RSS: %.4f'% sum((result_ARIMA.fittedvalues-ts_log_diff)**2))
	#plt.show()
	output = result_ARIMA.predict()


	#plotting results
	orig = plt.plot(agg_df, color='blue',label='Original')
	pred = plt.plot(output, color='black',label='Predicted')
	plt.legend(loc='best')
	plt.title('Actual Vs Predictions')
	plt.show()
	return output





def calculateResults(original, predictions):
	#Calculating Absolute percentage error
	ape_error = []
	awv_error = []
	for index in range(len(original)):
		err1 = abs((original['count'][index])-(predictions[index])) / (original['count'][index])
		err2 = abs((original['count'][index])-(predictions[index])) / (predictions[index])
		ape_error.append(err1)
		awv_error.append(err2)

	ape = (sum(ape_error)/len(ape_error))*100
	awv = (sum(awv_error)/len(awv_error))*100
	print("Absolute percentage error is : ", ape)
	print("Absolute weighted variance is : ", awv)


if __name__ == '__main__':
	inputFile = 'DC_2_Dataset_support_requests.json'
	train, test = read_data(inputFile)
	dataVisualization(train)
	test_stationarity(train)
	#ts_log_diff = differencing(train)
	ACF_PACF(train)
	#decomposition(agg_df)
	predictions = ARIMA_model(train,test)
	calculateResults(train, predictions)
