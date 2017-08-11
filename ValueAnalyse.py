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
			self.mean_exp = self.calculateAllEMA(self.values)
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
		k = float(2)/(number_of_period+1)
		return last_price * k + last_EMA *(1-k)

	def calculateAllEMA(self,values_array):
		df = pd.DataFrame(values_array, columns=['BTC', 'ETH', 'DASH'])
		# pour le moment on ne fait le calcul que pour une valeur : BTC
		# comment le faire pour chaque colonne de values_array
		# dfb = df['BTC']
		column_by_search = ["BTC", "ETH", "DASH"]
		for i,column in enumerate(column_by_search):
			ema=[]
			print("column")
			print(column)
			for i in range(0, len(column)-24):
				EMA_yesterday = column.iloc[1+j:22+j].mean()
				k = float(2)/(22+1)
				ema.append(column.iloc[23 + j]*k+EMA_yesterday*(1-k))
			mean_exp[j] = ema[-1]
		return mean_exp

	# quand le declenche t on ? Des le constructeur ou dans un main qui fait des appels reguliers ?
	def actionDecision(self):
		results = np.array([["",'BTC','ETH','DASH'],
						['Action',"","",""]])
		for i in range(1,len(self.lastValue)) :
			#print("self.lastValue : ",self.lastValue)
			if self.mean_exp:
				print("self.mean_exp")
				print("float(np.mean(self.fiveLast[0,i])) : ",float(np.mean(self.fiveLast[0,i])))
				print("-------------")
				print("moyenne : ", (float(np.mean(self.fiveLast[0,i]))))
				print("moyenne exp : ",(float(self.mean_exp[1,i])))
				if ((float(np.mean(self.fiveLast[0,i])) > (float(self.lastValue[i-1]))) and (float (self.mean_exp[1,i]) >float(self.lastValue[i-1]))):
					results[1,i]="sell"
				elif((float(self.fiveLast[1,i])< (float(self.lastValue[i-1]))) and (float(self.mean_exp[1,i])< float(self.lastValue[i-1]))):
					results[1,i]="buy"
		return results
					
					
					
#Moyenne exponentielle 
