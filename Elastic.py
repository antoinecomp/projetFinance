"""
Created on Sun June 25 09:02:36 2017

@author: muzinga
"""
import certifi
import threading
import urllib.request
from elasticsearch import Elasticsearch

class Elastic:
	def __init__(self,hosts,usr,password,port):
		self._hosts = hosts
		self._usr = usr
		self._password = password
		self._port=port
		self.es = Elasticsearch(hosts=hosts,http_auth=(usr,password),port=port,ca_certs=certifi.where())
		print(self.es)
		

	def store(self,assets,value):
		res = self.es.index(index="finance", doc_type=assets, body=value)
		return value
