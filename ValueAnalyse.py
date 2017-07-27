import json
import numpy as np
import pandas as pd

class ValueAnalyse:
	""""""
	
	def __init__(self,json_text):
		"""je recupere les valeurs du texte json"""	
		# on pourrait l'ameliorer en "
		self.bol=False
		print ("json_text : ")
		print (json_text)
		return
		self.values = [(each["BTC"].get("USD"), each["ETH"].get("USD"), each["DASH"].get("USD")) for each in json.loads(str(json_text))]
		if(len(self.values)>=24):
			self.bol = True
			mean_exp = calculateAllEMA(self.values)
		self.last_mean = calculateSMA(self.values)

		self.fiveLast = np.array(self.values[-5:])
		self.lastValue = self.values[-1]

		


	def calculateSMA(self,values_array):	
		df = pd.DataFrame(values_array, columns=['BTC', 'ETH', 'DASH'])		
		last_mean = np.array([["",'BTC','ETH','DASH'],
						['Mean',df['BTC'].tail(5).mean(),df['BTC'].tail(5).mean(),df['BTC'].tail(5).mean()]])
		return last_mean_array

	def calculateEMA(last_price,number_of_period,last_EMA):
		k = float(2)/(number_of_period+1)
		return last_price * k + last_price *(1-k)

	def calculateAllEMA(self,values_array):
		df = pd.DataFrame(values_array, columns=['BTC', 'ETH', 'DASH'])
		# pour le moment on ne fait le calcul que pour une valeur : BTC
		# comment le faire pour chaque colonne de values_array
		# dfb = df['BTC']
		for i,column in enumerate(df[column]):
			ema=[]
			for i in range(0, len(column)-24):
				EMA_yesterday = column.iloc[1+i:22+i].mean()
				k = float(2)/(22+1)
				ema.append(column.iloc[23 + i]*k+EMA_yesterday*(1-k))
			mean_exp[i] = ema[-1]
		return mean_exp

	# quand le declenche t on ? Des le constructeur ou dans un main qui fait des appels reguliers ?
	def actionDecision(self):
		results = np.array([["",'BTC','ETH','DASH'],
						['Action',"","",""]])
		for i in range(1,len(self.lastValue)+1) :
			if ((float(fiveLastMean[1,i]) > (float(self.lastValue[i-1]))) and (float (MeanExp[1,i]) >float(self.lastValue[i-1]))):
					results[1,i]="sell"
			elif((float(fiveLastMean[1,i])< (float(self.lastValue[i-1]))) and (float (MeanExp[1,i])< float(self.lastValue[i-1]))):
					results[1,i]="buy"
