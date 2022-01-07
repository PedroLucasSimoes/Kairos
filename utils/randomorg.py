import requests
import json
from pprint import pprint
import time
import sys
sys.path.append(".")
from exceptions import JSON_RPC_ERROR

class RandomData:
	
	def __init__(self, data):
		self.raw = data
		self.result = self.raw["result"]["random"]["data"]
		
	def getSum(self):
		sumOfAll = 0
		for i in self.result:
			sumOfAll += i
		return self.result, sumOfAll
		
	

def get(minimum: int, maximum: int, amt : int = 1) -> RandomData:
	raw_data = {
		"jsonrpc": "2.0",
		"method":"generateIntegers",
		"params": {
			"apiKey":"adecc923-7289-491c-8de1-ae80a865c29c",
			"n": amt,
			"min" : minimum,
			"max": maximum
		},
		"id":1
	}
	
	headers = {'Content-type': 'application/json','Content-Length': '200', 'Accept': 'application/json'}
	data = json.dumps(raw_data)
	
	response = requests.post(
	url='https://api.random.org/json-rpc/2/invoke',
	data=data,
	headers=headers
	)
	
	if response.status_code == 200:
		data = RandomData(response.json())
		#data = response.json()
		try:
			data.raw["error"]
		except Exception as e:
			return data
		else:
			raise JSON_RPC_ERROR(data)
