import json
import numpy as np
import pandas as pd

toDo=[[0,"Ordre de vente que EMC et SMC d'accord"],[1,"annonces de crash/solde"]]
print "TO DO :",toDo

# lire les donnees du fichier a chaque fois qu'il y a une nouvelle valeur et mettre les dernieres dans des tableaux 5,13 et la derniere dans lastValue
# https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,DASH&tsyms=USD

# Celle la envoi des requetes toutes les 3 sec
# Il faut arriver a faire le tableau suivant ou taper dans un fichier ou l'on prend les x dernieres valeur
if(False):
	def printit():
	  threading.Timer(3.0, printit).start()
	  f = urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR")
	  print(f.read())

	account_sid = "AC59592f7f0fb983ee92bb4d0aacfec1e2"
	auth_token = "9bf81090628c3206b39c8648eac91e1a"
	client = Client(account_sid, auth_token)


json_text = """
[
{"BTC":{"USD":2167.85},"ETH":{"USD":167.88},"DASH":{"USD":102.31}},
{"BTC":{"USD":2253.12},"ETH":{"USD":177.76},"DASH":{"USD":109.17}},
{"BTC":{"USD":2251.47},"ETH":{"USD":177.71},"DASH":{"USD":109.12}},
{"BTC":{"USD":2251.47},"ETH":{"USD":177.71},"DASH":{"USD":109.12}},
{"BTC":{"USD":2251.47},"ETH":{"USD":177.71},"DASH":{"USD":109.12}},
{"BTC":{"USD":2167.85},"ETH":{"USD":167.88},"DASH":{"USD":102.31}},
{"BTC":{"USD":2407.05},"ETH":{"USD":222.67},"DASH":{"USD":134.09}},
{"BTC":{"USD":2405.47},"ETH":{"USD":222.86},"DASH":{"USD":134.09}},
{"BTC":{"USD":2404.51},"ETH":{"USD":222.83},"DASH":{"USD":134.09}},
{"BTC":{"USD":2404.23},"ETH":{"USD":222.86},"DASH":{"USD":134.09}},
{"BTC":{"USD":2404.22},"ETH":{"USD":222.99},"DASH":{"USD":134.09}},
{"BTC":{"USD":2403.5},"ETH":{"USD":222.85},"DASH":{"USD":134.09}},
{"BTC":{"USD":2403.79},"ETH":{"USD":222.94},"DASH":{"USD":134.09}},
{"BTC":{"USD":2403.74},"ETH":{"USD":222.8},"DASH":{"USD":133.96}},
{"BTC":{"USD":2403.18},"ETH":{"USD":222.82},"DASH":{"USD":133.96}},
{"BTC":{"USD":2403.37},"ETH":{"USD":222.82},"DASH":{"USD":133.96}},
{"BTC":{"USD":2403.37},"ETH":{"USD":222.82},"DASH":{"USD":133.96}},
{"BTC":{"USD":2403.37},"ETH":{"USD":223.09},"DASH":{"USD":133.96}},
{"BTC":{"USD":2403.37},"ETH":{"USD":223.09},"DASH":{"USD":133.96}},
{"BTC":{"USD":2404.15},"ETH":{"USD":223.09},"DASH":{"USD":133.96}},
{"BTC":{"USD":2404.15},"ETH":{"USD":223.09},"DASH":{"USD":133.96}},
{"BTC":{"USD":2404.31},"ETH":{"USD":223.02},"DASH":{"USD":133.96}},
{"BTC":{"USD":2403.76},"ETH":{"USD":222.98},"DASH":{"USD":133.96}},
{"BTC":{"USD":2403.76},"ETH":{"USD":222.98},"DASH":{"USD":133.96}},
{"BTC":{"USD":2405.12},"ETH":{"USD":222.86},"DASH":{"USD":133.96}},
{"BTC":{"USD":2404.76},"ETH":{"USD":222.91},"DASH":{"USD":133.99}},
{"BTC":{"USD":2404.76},"ETH":{"USD":222.91},"DASH":{"USD":133.99}}
]
"""

a = json.loads(json_text)

values = [(each["BTC"].get("USD"), each["ETH"].get("USD"), each["DASH"].get("USD")) for each in a]

fiveLast = np.array(values[-5:])
lastValue = values[-1]

df = pd.DataFrame(values, columns=['BTC', 'ETH', 'DASH'])

# on calcule les moyennes sma, ema
# SMA:
def calculateSMA(prices):
	return prices.tail(5).mean()

MeanBTC = calculateSMA(df['BTC'])
MeanETH = calculateSMA(df['ETH'])
MeanDASH = calculateSMA(df['DASH'])

fiveLastMean = np.array([["",'BTC','ETH','DASH'],
						['Mean',MeanBTC,MeanETH,MeanDASH]])


# EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day).
# I have to store those values
# If I have the time I can manage it by indexing on it. 

# we take the closing prices for the first 22 days ## Why the first and not the last ?
# closingPricesBTC = df['BTC'].iloc[1:22].mean()
closingPricesETH = df['ETH'].iloc[-1:22].mean()
closingPricesDASH = df['DASH'].iloc[-1:22].mean()
# taking the following day s (day 23) closing price multiplied by k, then multiply the previous day s moving average by (1-k) and add the two.

def calculateEMA(todayPrice,numberOfDays,EMAYesterday):
	k = float(2)/(numberOfDays+1)
	return todayPrice * k + EMAYesterday *(1-k)

def calculateAllEMA(df):
	ema=[]
	for i in range(0, len(df)-24):
		EMAYesterday = df.iloc[1+i:22+i].mean()
		k = float(2)/(22+1)
		# print(str(i)+" "+str(len(ema)))
		ema.append(df.iloc[23 + i]*k+EMAYesterday*(1-k))
	return ema[-1]

MeanExpBTC = calculateAllEMA(df['BTC'])
MeanExpETH = calculateAllEMA(df['ETH'])
MeanExpDASH = calculateAllEMA(df['DASH'])

MeanExp = np.array([["",'BTC','ETH','DASH'],
						['Mean',MeanExpBTC,MeanExpETH,MeanExpDASH]])

#print "emaBTC : "
#print emaBTC
#print emaBTC["ETH"]

# on lance une alerte d'achat ou de vente en cas de pb
results = np.array([["",'BTC','ETH','DASH'],
						['Action',"","",""]])

for i in range(1,len(lastValue)+1) :
	if ((float(fiveLastMean[1,i]) and MeanExp[1,i]) > (float(lastValue[i-1]))):
		print "(fiveLastMean[1,i]) : ",float(fiveLastMean[1,i])
		print "MeanExp[1,i] : ",MeanExp[1,i]
		print "***"
		print "(float(lastValue[i-1]))", (float(lastValue[i-1]))
		print "sell",fiveLastMean[0,i]
		results[1,i]="sell" 

	elif((float(fiveLastMean[1,i]) and MeanExp[1,i])< (float(lastValue[i-1]))):
		print "fuck!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
		results[1,i]="buy"

print "---------------------------------------------------------"
print "lastValue : "
print(lastValue)
print "fiveLastMean : "
print(fiveLastMean)
print "MeanExp : "
print(MeanExp)
print "----------"
print "result : "
print results
buyExist = False
sellExist = False
print "---------------------------------------------------------"
j=0
k=0

# Creer deux tableaux vides de string

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

print "Vendre ",sellValue, " contre ",buyValue

# le prochain chantier est de mesurer lequel est le plus prometteur


# Ensuite on va faire un systeme pour prevenir quand un cours s'est casse la gueule
if(False):
	# il faut ajouter les parties qu'on echange : ex BTC -> ETH , donc peut-etre attendre
	# Envoi de texto
	message = client.api.account.messages.create(to="+33620050318",
		                                         from_="+33644601266",
		                                         body="Vendre "
												#,sellValue, " contre ",buyValue
												)



	# Connection a elasticsearch
	es = Elasticsearch(
		hosts=['localhost'],
		http_auth=('elastic', 'changeme'),
		port=9200,
		ca_certs=certifi.where()
	)
