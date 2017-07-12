import threading
from Elastic import Elastic
import urllib.request
from ValueAnalyse import ValueAnalyse 
class Util:
	def __init__(self):
		pass
	def disp(self,el,call,prices,assets):
		threading.Timer(1, self.disp,[el,call,prices,assets]).start()
		value = urllib.request.urlopen(call).read()
		prices.append(value)
		print(len(prices))
		print("prices : ")
		print(type(prices))
		a = " ".join(str(x) for x in prices)
		print(a)
		va = ValueAnalyse(a)
		el.store(assets,value)
