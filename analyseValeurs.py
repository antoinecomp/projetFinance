import json
import numpy as np
import pandas as pd

# lire les donnees du fichier a chaque fois qu'il y a une nouvelle valeur et mettre les dernieres dans des tableaux 5,13 et la derniere dans lastValue
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

values = [(each["BTC"].get("USD"), each["ETH"].get("USD"), each["DASH"].get("USD")) for each in a]

fiveLast = np.array(values[-5:])
lastValue = values[-1]

df = pd.DataFrame(values, columns=['BTC', 'ETH', 'DASH'])

# on calcule les moyennes sma, ema
# SMA: 
MeanBTC = df['BTC'].tail(5).mean()
MeanETH = df['ETH'].tail(5).mean()
MeanDASH = df['DASH'].tail(5).mean()

fiveLastMean = np.array([["",'BTC','ETH','DASH'],
						['Mean',MeanBTC,MeanETH,MeanDASH]])


# EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day).
# I have to store those values
# If I have the time I can manage it by indexing on it. 
#k = (float)2/(22+1)



# on lance une alerte d'achat ou de vente en cas de pb
result = np.array([["",'BTC','ETH','DASH'],
						['Action',"","",""]])

for i in range(1,len(lastValue)+1) :
	if (fiveLastMean[1,i] < lastValue[i-1]):
		result[1,i]="buy" 
	elif(fiveLastMean[1,i] > lastValue[i-1]):
		result[1,i]="sell"

print(fiveLastMean)
print(lastValue)
print result
