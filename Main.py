#Voici un exemple d'implementation de la classe util
#Ici on enregistre les réponse d'api dans un tableau (prices) toute les secondes

from Elastic import Elastic
from Util import Util
el = Elastic(['localhost'],'elastic', 'changeme',9200)

prices=[]
ut = Util()

ut.disp(el,"https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR",prices,'crypto')
