import threading
import numpy as np
from Elastic import Elastic
import urllib.request
from ValueAnalyse import ValueAnalyse
import json
 
class Util:
	def __init__(self):
		pass
	def disp(self,el,call,prices,assets):
		threading.Timer(1, self.disp,[el,call,prices,assets]).start()
		value = urllib.request.urlopen(call).read()
		prices.append(value)

		#print(len(prices))
		#print("prices : ")
		#print(type(prices))
		#a = " ".join(str(x) for x in prices)
		#print(a)

		# test
		if(False):
			json_text = """
			[
			{"BTC":{"USD":2167.85},"ETH":{"USD":167.88},"DASH":{"USD":102.31}},
			{"BTC":{"USD":2253.12},"ETH":{"USD":177.76},"DASH":{"USD":109.17}},
			{"BTC":{"USD":2251.47},"ETH":{"USD":177.71},"DASH":{"USD":109.12}},
			{"BTC":{"USD":2251.47},"ETH":{"USD":177.71},"DASH":{"USD":109.12}},
			{"BTC":{"USD":2251.47},"ETH":{"USD":177.71},"DASH":{"USD":109.12}},
			{"BTC":{"USD":2167.85},"ETH":{"USD":167.88},"DASH":{"USD":102.31}}
			]
			"""
			a = json.loads(json_text)

		json_text = "[" + ','.join([e.decode("utf-8") for e in prices]) + ']'
		#a = json.loads(json_text)


		va = ValueAnalyse(json_text)

		results = va.actionDecision()
		buyValue =(len(results[1])-1)*[""]
		sellValue = (len(results[1])-1)*[""]
	
		# on parcourt la deuxieme ligne
		for i in range(1,len(results[1])):
			if results[1][i] == "buy":
				buyExist = True
				# il me faut l'indice a acheter
				buyValue[k] = results[0][i]
				k=k+1
			if results[1][i] == "sell":
				sellExist = True
				sellValue[j] = results[0][i]
				j=j+1
			#if ((sellExist != 0) and (buyExist !=0)):
			#	break

		print("Vendre ")
		print(sellValue)
		print(" contre ")
		print (buyValue)		

		el.store(assets,value)
