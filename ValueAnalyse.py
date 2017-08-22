import json
import numpy as np
import pandas as pd

class ValueAnalyse:
	""""""
	
	def __init__(self,json_text):
		"""je recupere les valeurs du texte json"""	
		# on pourrait l'ameliorer en "
		self.bol=False
		#print ("json_text : ")
		#print (json_text)
		self.mean_exp =[]
		self.values = [(each["BTC"].get("USD"), each["ETH"].get("USD"), each["DASH"].get("USD")) for each in json.loads(str(json_text))]
		if(len(self.values)>=24):
			self.bol = True
			df = pd.DataFrame(self.values, columns=['BTC', 'ETH', 'DASH'])
			# self.mean_exp = self.calculateAllEMA(self.values)
			self.mean_exp = self.ewmas(df,24,False)
			print("self.mean_exp")
			print(self.mean_exp)
		self.last_mean = self.calculateSMA(self.values)

		self.fiveLast = np.array(self.values[-5:])
		if self.values:
			self.lastValue = self.values[-1]

		


	def calculateSMA(self,values_array):	
		df = pd.DataFrame(values_array, columns=['BTC', 'ETH', 'DASH'])		
		last_mean = np.array([["",'BTC','ETH','DASH'],
						['Mean',df['BTC'].tail(5).mean(),df['BTC'].tail(5).mean(),df['BTC'].tail(5).mean()]])
		return last_mean

	def calculateEMA(last_price,number_of_period,last_EMA):
		# Start by calculating k for the given timeframe. 2 / (22 + 1) = 0,0869
		k = float(2)/(number_of_period+1)
		return last_price * k + last_EMA *(1-k)

	def calculateAllEMA(self,values_array):
		df = pd.DataFrame(values_array, columns=['BTC', 'ETH', 'DASH'])
		column_by_search = ["BTC", "ETH", "DASH"]
		print(df)
		for i,column in enumerate(df[column]):
			ema=[]
			# over and over for each day that follows day 23 to get the full range of EMA
			#for i in range(0, len(column)-24): ??????????
			print("len(column)-24")
			print(len(column)-24)
			for j in range(0, len(column)-24):
				print("IN THE LOOOOOOP")
				# Add the closing prices for the first 22 days together and divide them by 22.
				EMA_yesterday = column.iloc[1+j:22+j].mean()
				k = float(2)/(22+1)
				# getting the first EMA day by taking the following day’s (day 23) closing price multiplied by k, then multiply the previous day’s moving average by (1-k) and add the two.
				ema.append(column.iloc[23 + j]*k+EMA_yesterday*(1-k))
			print("ema")
			print(ema)
			mean_exp[i] = ema[-1]
		return mean_exp

	# quand le declenche t on ? Des le constructeur ou dans un main qui fait des appels reguliers ?
	def actionDecision(self):
		results = np.array([["",'BTC','ETH','DASH'],
						['Action',"","",""]])
		print("self.lastValue")
		print(self.lastValue)
		for i in range(0,len(self.lastValue)) :
			#print("self.lastValue : ",self.lastValue)
			if(len(self.mean_exp) != 0):
				print("-------------")
				if ((float(np.mean(self.fiveLast[0,i])) > (float(self.lastValue[i]))) and (float (self.mean_exp.iloc[1,i]) >float(self.lastValue[i]))):
					print("*****SELL******")
					print("valeur teste : ",(float(self.lastValue[i])))
					print("moyenne : ", (float(np.mean(self.fiveLast[0,i]))))
					print("moyenne exp : ",(float(self.mean_exp.iloc[1][i])))
					results[1,i+1]="sell"
				elif((float(self.fiveLast[1,i])< (float(self.lastValue[i]))) and (float(self.mean_exp.iloc[1,i])< float(self.lastValue[i]))):
					print("*****BUY******")
					print("valeur teste : ",(float(self.lastValue[i])))
					print("moyenne : ", (float(np.mean(self.fiveLast[0,i]))))
					print("moyenne exp : ",(float(self.mean_exp.iloc[1][i])))
					results[1,i+1]="buy"
		print("results : ",results)
		print("-------------")
		return results
	def ewmas(self,df, win, keepSource):
		"""Add exponentially weighted moving averages for all columns in a dataframe.

		Arguments: 
		df -- pandas dataframe
		win -- length of ewma estimation window
		keepSource -- True or False for keep or drop source data in output dataframe

		"""

		df_temp = df.copy()
		# Manage existing column names
		colNames = list(df_temp.columns.values).copy()
		removeNames = colNames.copy()

		i = 0
		for col in colNames:

		    # Make new names for ewmas
		    ewmaName = colNames[i] + '_ewma_' + str(win)   

		    # Add ewmas
		    df_temp[ewmaName] = pd.stats.moments.ewma(df[colNames[i]], span = win)
		    i = i + 1

		# Remove estimates with insufficient window length
		df_temp = df_temp.ix[win:]

		# Remove of keep source data
		if keepSource == False:
		    df_temp = df_temp.drop(removeNames,1)

		return df_temp
					
					
					
#Moyenne exponentielle 
# playback sex
