import json
import numpy as np
import pandas as pd

class Hey:
	""""""
	
	def __init__(json_text):
		"""je récupère les valeurs du texte json"""	
		# on pourrait l'améliorer en "
		self.values = [(each["BTC"].get("USD"), each["ETH"].get("USD"), each["DASH"].get("USD")) for each in json.loads(json_text)]
		self.last_mean = calculateSMA(self.values)
		mean_exp = calculateAllEMA(self.values)
		
	def calculateSMA(values_array):	
		df = pd.DataFrame(values_array, columns=['BTC', 'ETH', 'DASH'])		
		last_mean = np.array([["",'BTC','ETH','DASH'],
						['Mean',df['BTC'].tail(5).mean(),df['BTC'].tail(5).mean(),df['BTC'].tail(5).mean()]])
		return last_mean_array

	def calculateEMA(last_price,number_of_period,last_EMA):
		k = float(2)/(number_of_period+1)
		return last_price * k + last_price *(1-k)

	def calculateAllEMA(values_array):
		df = pd.DataFrame(values_array, columns=['BTC', 'ETH', 'DASH'])
		# pour le moment on ne fait le calcul que pour une valeur : BTC
		# comment le faire pour chaque colonne de values_array
		# dfb = df['BTC']
		for i,column in enumerate(df[column])
			ema=[]
			for i in range(0, len(column)-24):
				EMA_yesterday = column.iloc[1+i:22+i].mean()
				k = float(2)/(22+1)
				ema.append(column.iloc[23 + i]*k+EMA_yesterday*(1-k))
			mean_exp[i] = ema[-1]
		return mean_exp

	# quand le declenche t on ? Des le constructeur ou dans un main qui fait des appels reguliers ?
	def actionDecision()
		results = np.array([["",'BTC','ETH','DASH'],
						['Action',"","",""]])
		for i in range(1,len(lastValue)+1) :
			if ((float(fiveLastMean[1,i]) > (float(lastValue[i-1]))) and (float (MeanExp[1,i]) >float(lastValue[i-1]))):
					results[1,i]="sell"
			elif((float(fiveLastMean[1,i])< (float(lastValue[i-1]))) and (float (MeanExp[1,i])< float(lastValue[i-1]))):
					results[1,i]="buy"

	# manque une classe ?
