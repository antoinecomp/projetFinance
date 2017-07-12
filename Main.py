from Elastic import Elastic
from Util import Util
el = Elastic(['localhost'],'elastic', 'changeme',9200)

prices=[]
#el.store('crypto',"https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR",prices)
ut = Util()

ut.disp(el,"https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR",prices,'crypto')

