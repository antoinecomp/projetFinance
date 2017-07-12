import json
import numpy as np
import pandas as pd

class ValueAnalyse:
	""""""
	
	def __init__(self,json_text):
		"""je recupere les valeurs du texte json"""	
		# on pourrait l'ameliorer en "
		self.bol=False
		self.values = [(each["BTC"].get("USD"), each["ETH"].get("USD"), each["DASH"].get("USD")) for each in json.loads(str(json_text))]
		if(len(self.values)>=24):
			self.bol = True

