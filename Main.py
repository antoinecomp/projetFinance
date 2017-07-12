#Voici un exemple d'implementation de la classe util
#Ici on enregistre les reponse d'api dans un tableau (prices) toute les secondes
import ValueAnalyse

from Elastic import Elastic
from Util import Util

el = Elastic(['localhost'],'elastic', 'changeme',9200)

prices=[]

newAnalyse = ValueAnalyse(prices)
arrayAction = newAnalyse.actionDecision()

print "There has been some changes, you can do :"
print arrayAction


# a quoi ser ut = Util() ?
ut = Util()

# Quand prices a change on fait appel a la classe d'analyse

ut.disp(el,"https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR",prices,'crypto')
